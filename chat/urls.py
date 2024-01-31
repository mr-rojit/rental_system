from django.urls import path
from .views import chat_home, chat_people, send_chat
urlpatterns = [
    path('', chat_home, name='chat_home' ),
    path('<int:pk>/', chat_people, name='chat_people' ),
    path('send/', send_chat, name='send_chat'),

]