from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Party
from .serializers import PartySerializer
from django.shortcuts import get_object_or_404


class PartyCreateView(generics.CreateAPIView):
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['creator'] = request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        party = serializer.save(creator=self.request.user)
        party.users.add(self.request.user)


class PartyJoinView(generics.GenericAPIView):
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        party = get_object_or_404(Party, pk=pk)
        user = request.user

        # Check if the user is already in the party
        if party.users.filter(id=user.id).exists():
            return Response({"detail": "User already in the party"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user has enough balance
        if user.solde < party.min_amount:
            return Response({"detail": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)

        # Deduct the min_amount from the user's balance
        user.solde -= party.min_amount
        user.save()

        # Add the user to the party
        party.users.add(user)

        return Response({"detail": "Successfully joined the party"}, status=status.HTTP_200_OK)
