from decimal import Decimal
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

        # Vérifiez si l'utilisateur a suffisamment de solde avant de créer la partie
        min_amount = data.get('min_amount', 0)
        if request.user.solde < Decimal(min_amount):
            return Response({"detail": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        party = serializer.save(creator=self.request.user)

        # Deduct the min_amount from the user's balance and save
        self.request.user.solde -= party.min_amount
        self.request.user.save()

        # Add the creator to the party users
        party.users.add(self.request.user)
    
class PartyDetailView(generics.RetrieveAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            party = self.get_object()
            serializer = self.get_serializer(party)
            return Response(serializer.data)
        except Party.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        


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


class PartyQuitView(generics.GenericAPIView):
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        party = get_object_or_404(Party, pk=pk)
        user = request.user

        # Check if the user is in the party
        if not party.users.filter(id=user.id).exists():
            return Response({"detail": "User not in the party"}, status=status.HTTP_400_BAD_REQUEST)

        # Remove the user from the party
        party.users.remove(user)

        # Optionally refund the min_amount to the user's balance
        # This assumes a full refund; TODO: adjust logic if a partial refund is required
        user.solde += party.min_amount
        user.save()

        return Response({"detail": "Successfully left the party"}, status=status.HTTP_200_OK)