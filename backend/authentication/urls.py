from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,UserView, accept_friendship_invitation, check_unique, check_auth, get_friendship_invitations, reject_friendship_invitation, get_friendship_amis, get_balance

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-unique/<str:field>/<str:value>/',
         check_unique, name='check_unique'),

    # Endpoint sécurisé avec DRF
    path('balance/', get_balance, name='get_balance'),
    path('check-auth/', check_auth, name='check_auth'),
    path('friendship/amis/', get_friendship_amis, name='get_friendship_invitations'),
    path('friendship/invitations/', get_friendship_invitations, name='get_friendship_invitations'),
    path('friendship/invitations/<int:invitation_id>/accept/', accept_friendship_invitation, name='accept_friendship_invitation'),
    path('friendship/invitations/<int:invitation_id>/reject/', reject_friendship_invitation, name='reject_friendship_invitation'),
    path('user/', UserView.as_view(), name='user')
]
