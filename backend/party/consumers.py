from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PokerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.party_id = self.scope['url_route']['kwargs']['party_id']
        self.room_group_name = f'poker_{self.party_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Notify others that a new player has joined
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'player_join',
                'player': self.scope['user'].id  # Send the user's ID
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user_id': self.scope['user'].id  # Include the user ID in messages
            }
        )

    async def player_join(self, event):
        player = event['player']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'player_join',
            'player': player
        }))

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'user_id': event['user_id']  # Include the user ID in messages
        }))
