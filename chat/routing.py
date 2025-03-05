from django.urls import path
from chat.consumers import Chatconsumer

wsPattern = [
    path("ws/messages/<str:room_name>/", Chatconsumer.as_asgi())
]