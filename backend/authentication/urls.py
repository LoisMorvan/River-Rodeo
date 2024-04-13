from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, check_unique

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-unique/<str:field>/<str:value>/',
         check_unique, name='check_unique'),
]
