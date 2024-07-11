from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from knox.views import LogoutView as KnoxLogoutView
from rest_framework.generics import GenericAPIView
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken

from backend.authentication.models import CustomUser, Friendship
from .serializers import FriendshipSerializer, RegistrationSerializer, LoginSerializer, CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class UserView(GenericAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)

        # Use the CustomUserSerializer to serialize the user instance
        user_serializer = CustomUserSerializer(user)

        return Response({
            "user": user_serializer.data,
            "token": token
        }, status=status.HTTP_200_OK)


class LogoutView(KnoxLogoutView):
    permission_classes = ()


def check_unique(request, field, value):
    User = get_user_model()
    is_unique = not User.objects.filter(**{f'{field}__iexact': value}).exists()
    return JsonResponse({'is_unique': is_unique})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    # Si le middleware a déjà validé le token, l'utilisateur est authentifié
    return Response({'message': 'Authenticated'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_friendship_amis(request):
    user = request.user
    amis_from = Friendship.objects.filter(to_user=user, status='accepted').values_list('from_user__username', flat=True)
    amis_to = Friendship.objects.filter(from_user=user, status='accepted').values_list('to_user__username', flat=True)
    
    amis_list = list(amis_from) + list(amis_to)
    
    return Response(amis_list, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_friendship_invitations(request):
    user = request.user
    invitations = Friendship.objects.filter(to_user=user, status='pending')
    serializer = FriendshipSerializer(invitations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_friendship_invitation(request, invitation_id):
    invitation = get_object_or_404(Friendship, pk=invitation_id, to_user=request.user, status='pending')
    invitation.status = 'accepted'
    invitation.save()
    return Response({'message': 'Invitation accepted successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_friendship_invitation(request, invitation_id):
    invitation = get_object_or_404(Friendship, pk=invitation_id, to_user=request.user, status='pending')
    invitation.status = 'rejected'
    invitation.save()
    return Response({'message': 'Invitation rejected successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request):
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
    from_user = request.user
    to_user = get_object_or_404(CustomUser, username=username)
    existing_request = Friendship.objects.filter(from_user=from_user, to_user=to_user)
    if existing_request.exists():
        return Response({'error': 'Friendship request already exists'}, status=status.HTTP_400_BAD_REQUEST)
    new_request = Friendship.objects.create(from_user=from_user, to_user=to_user, status='pending')
    serializer = FriendshipSerializer(new_request)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_balance(request):
    user = request.user
    return JsonResponse({'balance': user.solde})