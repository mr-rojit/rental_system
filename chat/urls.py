from django.urls import path
from .views import chat_home, chat_people, send_chat, get_or_create_channel
urlpatterns = [
    path('', chat_home, name='chat_home' ),
    path('<int:pk>/', chat_people, name='chat_people' ),
    path('send/', send_chat, name='send_chat'),
    path('check_chat/<int:pk>/', get_or_create_channel, name='check_chat'),
]