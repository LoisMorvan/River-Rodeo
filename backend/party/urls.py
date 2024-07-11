from django.urls import path
from .views import PartyCreateView, PartyDetailView, PartyJoinView, PartyQuitView

urlpatterns = [
    path('create/', PartyCreateView.as_view(), name='party-create'),
    path('join/<int:pk>/', PartyJoinView.as_view(), name='party-join'),
    path('quit/<int:pk>/', PartyQuitView.as_view(), name='party-quit'),
    path('<int:id>/', PartyDetailView.as_view(), name='party-detail'),
]
