from django.urls import path
from .views import PartyCreateView, PartyDetailView, PartyJoinView, PartyQuitView, StartRoundView, DealCardsView, DealCommunityCardView, PlaceBetView, DetermineWinnerView

urlpatterns = [
    path('create/', PartyCreateView.as_view(), name='party-create'),
    path('join/<int:pk>/', PartyJoinView.as_view(), name='party-join'),
    path('quit/<int:pk>/', PartyQuitView.as_view(), name='party-quit'),
    path('<int:id>/', PartyDetailView.as_view(), name='party-detail'),
    path('start_round/<int:party_id>/',
         StartRoundView.as_view(), name='start-round'),
    path('deal_cards/<int:round_id>/',
         DealCardsView.as_view(), name='deal-cards'),
    path('deal_community_card/<int:round_id>/<str:stage>/',
         DealCommunityCardView.as_view(), name='deal-community-card'),
    path('place_bet/<int:round_id>/', PlaceBetView.as_view(), name='place-bet'),
    path('determine_winner/<int:round_id>/',
         DetermineWinnerView.as_view(), name='determine-winner'),
]
