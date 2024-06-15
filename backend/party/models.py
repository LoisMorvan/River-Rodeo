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


class Round(models.Model):
    party = models.ForeignKey(
        Party, related_name='rounds', on_delete=models.CASCADE)
    dealer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='won_rounds', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Pot(models.Model):
    round = models.ForeignKey(
        Round, related_name='pots', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
