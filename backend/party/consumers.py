from channels.generic.websocket import AsyncWebsocketConsumer
import json


class PokerConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.party_id = self.scope['url_route']['kwargs']['party_id']
        self.party_group_name = f'poker_party_{self.party_id}'

        # Joindre le groupe WebSocket spécifique à la partie
        await self.channel_layer.group_add(
            self.party_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Quitter le groupe WebSocket spécifique à la partie
        await self.channel_layer.group_discard(
            self.party_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Gérer les messages WebSocket reçus
        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        # Exemple d'action : mise à jour de l'état du jeu
        if action == 'update_game_state':
            game_state = text_data_json['game_state']

            # Envoyer l'état du jeu mis à jour à tous les clients du groupe
            await self.channel_layer.group_send(
                self.party_group_name,
                {
                    'type': 'game_state_update',
                    'game_state': game_state
                }
            )

    async def game_state_update(self, event):
        # Envoyer un message de mise à jour d'état de jeu à tous les clients connectés au groupe
        game_state = event['game_state']

        # Envoyer le message au WebSocket
        await self.send(text_data=json.dumps({
            'action': 'update_game_state',
            'game_state': game_state
        }))
