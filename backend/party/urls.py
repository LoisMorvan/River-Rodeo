from django.urls import path
from .views import PartyCreateView, PartyJoinView

urlpatterns = [
    path('create/', PartyCreateView.as_view(), name='party-create'),
    path('join/<int:pk>/', PartyJoinView.as_view(), name='party-join'),
]
