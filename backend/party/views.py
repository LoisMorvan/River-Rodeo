from treys import Card, Evaluator
from decimal import Decimal
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import random

from .models import Party, Round, PlayerHand, CommunityCard, Bet, GameState, PlayerBalance
from .serializers import PartySerializer, RoundSerializer, PlayerHandSerializer, CommunityCardSerializer


def deal_deck(number_of_cards):
    suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T',
              'J', 'Q', 'K', 'A']  # 2-9, Ten, Jack, Queen, King, Ace
    deck = [v + s for v in values for s in suits]
    random.shuffle(deck)
    return deck[:number_of_cards]


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

        PlayerBalance.objects.create(
            party=party, player=self.request.user, balance=party.min_amount)

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
            player_balances = {user.username: PlayerBalance.objects.get(
                party=party, player=user).balance for user in party.users.all()}
            response_data = serializer.data
            response_data['player_balances'] = player_balances
            return Response(response_data)
        except Party.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        except PlayerBalance.DoesNotExist:
            return Response({"detail": "Player balance not found."}, status=status.HTTP_404_NOT_FOUND)


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
        PlayerBalance.objects.create(
            party=party, player=user, balance=party.min_amount)

        return Response({"detail": "Successfully joined the party"}, status=status.HTTP_200_OK)


class StartRoundView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, party_id):
        party = get_object_or_404(Party, id=party_id)

        if not party.is_active:
            return Response({"detail": "Party is not active"}, status=status.HTTP_400_BAD_REQUEST)

        if party.has_active_round():
            return Response({"detail": "An active round is already in progress"}, status=status.HTTP_400_BAD_REQUEST)

        if party.users.count() < 2:
            return Response({"detail": "Not enough players to start a round"}, status=status.HTTP_400_BAD_REQUEST)

        round = Round.objects.create(party=party, dealer=party.creator)
        GameState.objects.create(
            round=round, current_turn=party.creator, stage="preflop")
        return Response(RoundSerializer(round).data, status=status.HTTP_201_CREATED)


class DealCardsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, round_id):
        round = get_object_or_404(Round, id=round_id)
        players = round.party.users.all()

        if PlayerHand.objects.filter(round=round).exists():
            return Response({"detail": "Cards already dealt"}, status=status.HTTP_400_BAD_REQUEST)

        for player in players:
            PlayerHand.objects.create(
                round=round, player=player, cards=deal_deck(2))

        player_hands = PlayerHand.objects.filter(round=round)
        serialized_hands = PlayerHandSerializer(player_hands, many=True).data

        return Response({
            "detail": "Cards dealt to all players",
            "player_hands": serialized_hands
        }, status=status.HTTP_201_CREATED)


class DealCommunityCardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, round_id, stage):
        round = get_object_or_404(Round, id=round_id)

        if stage not in ["flop", "turn", "river"]:
            return Response({"detail": "Invalid stage"}, status=status.HTTP_400_BAD_REQUEST)

        if CommunityCard.objects.filter(round=round, stage=stage).exists():
            return Response({"detail": f"{stage} cards already dealt"}, status=status.HTTP_400_BAD_REQUEST)

        if stage == "flop":
            cards = deal_deck(3)
        else:
            cards = [deal_deck(1)[0]]

        for card in cards:
            CommunityCard.objects.create(round=round, card=card, stage=stage)

        community_cards = CommunityCard.objects.filter(round=round)
        serialized_community_cards = CommunityCardSerializer(
            community_cards, many=True).data

        return Response({
            "detail": f"{stage.capitalize()} cards dealt",
            "community_cards": serialized_community_cards
        }, status=status.HTTP_201_CREATED)


class PlaceBetView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, round_id):
        round = get_object_or_404(Round, id=round_id)
        game_state = get_object_or_404(GameState, round=round)
        user = request.user
        amount = Decimal(request.data.get('amount'))
        action = request.data.get('action')  # 'bet', 'check', 'fold'

        if action not in ['bet', 'check', 'fold']:
            return Response({"detail": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

        player_balance = get_object_or_404(
            PlayerBalance, party=round.party, player=user)

        if action == 'bet':
            if player_balance.balance < amount:
                return Response({"detail": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
            if amount <= game_state.current_bet:
                return Response({"detail": "Bet must be higher than the current bet"}, status=status.HTTP_400_BAD_REQUEST)

            Bet.objects.create(round=round, player=user, amount=amount)
            player_balance.balance -= amount
            player_balance.save()

            if user.id not in game_state.player_bets:
                game_state.player_bets[user.id] = 0
            game_state.player_bets[user.id] += amount
            game_state.pot += amount
            game_state.current_bet = max(game_state.player_bets.values())

        elif action == 'check':
            if game_state.current_bet > game_state.player_bets.get(user.id, 0):
                return Response({"detail": "Cannot check, must call or raise to match the current bet"}, status=status.HTTP_400_BAD_REQUEST)
            # No state change for check, just move to the next player

        elif action == 'fold':
            game_state.folded_players.add(user)

        next_player = self.get_next_player(game_state, user)
        game_state.current_turn = next_player
        game_state.save()

        return Response({"detail": "Action processed"}, status=status.HTTP_201_CREATED)

    def get_next_player(self, game_state, current_player):
        players = list(game_state.active_players.exclude(
            id__in=game_state.folded_players.all()))
        if not players:
            return None
        current_index = players.index(current_player)
        next_index = (current_index + 1) % len(players)
        return players[next_index]


class DetermineWinnerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, round_id):
        round = get_object_or_404(Round, id=round_id)
        if round.is_over:
            return Response({"detail": "Round is already over"}, status=status.HTTP_400_BAD_REQUEST)

        community_cards = CommunityCard.objects.filter(round=round)
        hands = PlayerHand.objects.filter(round=round)

        best_hand, best_player = self.determine_best_hand(
            hands, community_cards)
        round.winner = best_player
        round.is_active = False
        round.is_over = True
        round.save()

        game_state = GameState.objects.get(round=round)

        player_balance = PlayerBalance.objects.get(
            party=round.party, player=best_player)
        player_balance.balance += game_state.pot
        player_balance.save()

        return Response({"detail": f"Winner determined: {best_player.username}"}, status=status.HTTP_200_OK)

    def determine_best_hand(self, hands, community_cards):
        evaluator = Evaluator()
        community = [Card.new(self.convert_card(card.card))
                     for card in community_cards]

        best_rank = float('inf')
        best_hand = None
        best_player = None

        for hand in hands:
            player_hand = [Card.new(self.convert_card(card))
                           for card in hand.cards]
            rank = evaluator.evaluate(community, player_hand)

            if rank < best_rank:
                best_rank = rank
                best_hand = hand
                best_player = hand.player

        return best_hand, best_player

    def convert_card(self, card):
        return card[0] + card[1].lower()


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

        # Retrieve the player's balance for the party
        player_balance = get_object_or_404(
            PlayerBalance, party=party, player=user)

        # Refund the remaining balance to the user's solde
        user.solde += player_balance.balance
        user.save()

        return Response({"detail": "Successfully left the party"}, status=status.HTTP_200_OK)
