from django.db import models
from django.conf import settings


class Party(models.Model):
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_parties', on_delete=models.CASCADE)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='joined_parties', blank=True)

    def __str__(self):
        return f'Party {self.id} created by {self.creator}'

    def has_active_round(self):
        return self.rounds.filter(is_active=True).exists()


class Round(models.Model):
    party = models.ForeignKey(
        Party, related_name='rounds', on_delete=models.CASCADE)
    dealer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='won_rounds', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_over = models.BooleanField(default=False)


class Pot(models.Model):
    round = models.ForeignKey(
        Round, related_name='pots', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class PlayerHand(models.Model):
    round = models.ForeignKey(
        Round, related_name='hands', on_delete=models.CASCADE)
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='hands', on_delete=models.CASCADE)
    cards = models.JSONField()


class CommunityCard(models.Model):
    round = models.ForeignKey(
        Round, related_name='community_cards', on_delete=models.CASCADE)
    card = models.CharField(max_length=5)
    stage = models.CharField(max_length=10)  # "flop", "turn", or "river"


class Bet(models.Model):
    round = models.ForeignKey(
        Round, related_name='bets', on_delete=models.CASCADE)
    player = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='bets', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class GameState(models.Model):
    round = models.OneToOneField(
        Round, related_name='state', on_delete=models.CASCADE)
    current_bet = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    current_turn = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='current_turn', on_delete=models.SET_NULL, null=True)
    # "preflop", "flop", "turn", or "river"
    stage = models.CharField(max_length=10)
    pot = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active_players = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='active_in_round')
    folded_players = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='folded_in_round')
    # to track each player's current bet amount
    player_bets = models.JSONField(default=dict)
