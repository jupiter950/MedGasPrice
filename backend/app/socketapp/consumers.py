import json
import requests
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import GasData
from .serializers import GasSerializer

class ChatConsumer(AsyncWebsocketConsumer):
    count = 1
    async def connect(self):
        print("connect...")
        await self.accept()
        self.send_gas_data_task = asyncio.ensure_future(self.send_gas_data())
            
    async def disconnect(self, close_code):
        if hasattr(self, 'send_gas_data_task'):
            self.send_gas_data_task.cancel()
        await self.close()

    async def receive(self, text_data):
        pass

    async def send_gas_data(self):
        while True:
            await self.send_gas_data_once()
            await asyncio.sleep(1800)

    async def send_gas_data_once(self):
        try:
            self.count = self.count + 1
            # await self.delete_gas_data()
            # await self.get_gas_data()
            await self.send(text_data=json.dumps({'status' : self.count}))
        except Exception as e:
            print("Error occurred while sending gas data:", e)
            
    @database_sync_to_async
    def delete_gas_data(self):
        GasData.objects.all().delete()
    @database_sync_to_async
    def get_gas_data(self):
        headers = {"Content-Type": "application/json; charset=utf-8",
                   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTEwODIwNDUsImV4cCI6MTcxMTI1NDg0NSwiaXNzIjoiUm91dGVzY2FuQXBpIiwic3ViIjoiNDUuMTI2LjMuMjUyIn0._GR9VFjPpS9nGfv--B7Y_n3sG-nBP38YDdswAvKjYAY"}
        res = requests.get('https://cdn.routescan.io/api/evm/all/aggregations/avg-gas-price?ecosystem=avalanche', headers=headers)
        print(res)  