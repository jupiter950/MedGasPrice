from django.urls import path

from . import consumers

ws_urlpatterns = [
    path(r'ws/test/', consumers.ChatConsumer.as_asgi()),
]