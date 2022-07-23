import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from accounts.models import CustomUser 
from .models import Chat 

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.self_id=self.scope["user"].id
        self.self_room="chat_room_"+str(self.self_id)

        self.other_user_id=self.scope["url_route"]["kwargs"]["id"]
        self.other_user_room="chat_room_"+str(self.other_user_id)
        

        await self.channel_layer.group_add(
            self.self_room,
            self.channel_name
        )
        await self.accept()

    
    async def receive(self, text_data=None, bytes_data=None):
        data=json.loads(text_data)
        message=data.get("message")
        response={
            "message":message,
            "sender":self.self_id,
             "receiver":self.other_user_id
        }

        await self.channel_layer.group_send(
            self.self_room,{
                "type":"send_message",
                "data":json.dumps(response)
            }
        )
        await self.channel_layer.group_send(
            self.other_user_room,{
                "type":"send_message",
                "data":json.dumps(response)
            }
        )

        sender_obj=await self.get_user_obj(self.self_id)
        receiver_obj=await self.get_user_obj(self.other_user_id)
        if sender_obj and receiver_obj:
            await self.create_message(sender_obj,receiver_obj,message)

    async def disconnect(self, code):
        print("Disconnected")

    
    async def send_message(self,event):
        data=json.loads(event["data"])
        await self.send(json.dumps(data))

    

    @database_sync_to_async
    def get_user_obj(self,id):
        obj=CustomUser.objects.filter(id=id)
        if obj.exists():
            obj=obj.first()
        return obj 

    
    @database_sync_to_async
    def create_message(self,sender,receiver,message):
        Chat.objects.create(sender=sender,receiver=receiver,message=message)