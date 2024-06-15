from rest_framework import serializers
from .models import Party, Round, Pot


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['id', 'min_amount',
                  'creator', 'created_at', 'is_active']
        read_only_fields = ['creator', 'created_at', 'is_active']


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'party', 'dealer', 'winner', 'created_at', 'is_active']


class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ['id', 'round', 'amount', 'created_at']
