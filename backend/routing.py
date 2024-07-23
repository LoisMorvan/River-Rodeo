from django.urls import path
from channels.routing import URLRouter
from .party.consumers import PokerConsumer

websocket_urlpatterns = [
    path('ws/poker/<int:party_id>/', PokerConsumer.as_asgi()),
]

application = URLRouter(websocket_urlpatterns)
