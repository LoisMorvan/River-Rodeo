from django.urls import re_path
from .party.consumers import PokerConsumer

websocket_urlpatterns = [
    re_path(r'ws/poker/(?P<party_id>\d+)/$', PokerConsumer.as_asgi()),
]