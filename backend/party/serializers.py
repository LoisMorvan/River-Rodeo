from rest_framework import serializers
from .models import Party, Round, Pot, PlayerHand, CommunityCard, Bet, GameState


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['id', 'min_amount', 'creator', 'created_at', 'is_active']
        read_only_fields = ['creator', 'created_at', 'is_active']


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'party', 'dealer', 'winner', 'created_at', 'is_active']


class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ['id', 'round', 'amount', 'created_at']


class PlayerHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerHand
        fields = ['id', 'round', 'player', 'cards']


class CommunityCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityCard
        fields = ['id', 'round', 'card', 'stage']


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ['id', 'round', 'player', 'amount', 'created_at']


class GameStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameState
        fields = ['id', 'round', 'current_bet', 'current_turn',
                  'stage', 'pot', 'active_players', 'player_bets']
        read_only_fields = ['round', 'current_turn', 'pot', 'player_bets']
