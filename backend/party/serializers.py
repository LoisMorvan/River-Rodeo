from rest_framework import serializers
from .models import Party, Round, Pot


class PartySerializer(serializers.ModelSerializer):
    user_usernames = serializers.SerializerMethodField()
    class Meta:
        model = Party
        fields = ['id', 'min_amount',
                  'creator', 'created_at', 'is_active','user_usernames']
        read_only_fields = ['creator', 'created_at', 'is_active']

    def get_user_usernames(self, obj):
        return [user.username for user in obj.users.all()]

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'party', 'dealer', 'winner', 'created_at', 'is_active']


class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ['id', 'round', 'amount', 'created_at']
