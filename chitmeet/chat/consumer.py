import json
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import DatabaseSyncToAsync

from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected!", event)

        other = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        thread, _ = await sync_to_async(Thread.objects.get_or_new)(me, other)
        self.chatroom = f'thread_{thread.id}'
        await self.channel_layer.group_add( self.chatroom, self.channel_name)

        await self.send( { "type" : "websocket.accept" } )
    
    async def websocket_receive(self, event):
        print("Websocket Message Received!", event)
        
        await self.channel_layer.group_send(
            self.chatroom,
            {
                "type" : "send_msg",
                "text": f'{event["text"]} by {self.scope["user"]}',
            }
        )
    
    async def send_msg(self, event):
        print('message', event)
        await self.send({
            "type" : "websocket.send",
            "text" : event["text"]
        })
    
    async def websocket_disconnect(self, event):
        print("Websocket Disconnected!", event)


