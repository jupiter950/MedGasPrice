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
            await asyncio.sleep(10)

    async def send_gas_data_once(self):
        try:
            self.count = self.count + 1
            await self.delete_gas_data()
            await self.get_gas_data()
            await self.send(text_data=json.dumps({'status' : self.count}))
        except Exception as e:
            print("Error occurred while sending gas data:", e)
            
    @database_sync_to_async
    def delete_gas_data(self):
        GasData.objects.all().delete()
    @database_sync_to_async
    def get_gas_data(self):
        res = requests.get('https://api.routescan.io/v2/network/mainnet/evm/333000333/transactions?sort=desc')
        for item in json.loads(res.text)['items']:
            serializer = GasSerializer(data={
                'tid': item['id'],
                'chainId': item['chainId'],
                'timestamp': item['timestamp'],
                'blockNumber': item['blockNumber'],
                'gasPrice': item['gasPrice'],
                'status': item['status'],
                'burnedFees': item['burnedFees'],
                'value': item['value'],
                'index': item['index'],
                'cfrom': item['from'],
                'fto': item['to']
            })
            if serializer.is_valid(raise_exception=True):
                serializer.save()