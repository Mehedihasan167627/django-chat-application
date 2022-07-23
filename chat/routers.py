from django.urls import path 
from .consumers import ChatConsumer

ws_patterns=[
      path("ws/chat/<int:id>/",ChatConsumer.as_asgi()),
]