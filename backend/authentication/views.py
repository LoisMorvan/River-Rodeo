from django.http import JsonResponse
from django.contrib.auth import get_user_model
from knox.views import LogoutView as KnoxLogoutView
from rest_framework.generics import GenericAPIView
from rest_framework import generics, status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
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
