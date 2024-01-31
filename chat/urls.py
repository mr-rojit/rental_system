from django.urls import path
from .views import chat_home, chat_people
urlpatterns = [
    path('', chat_home, name='chat_home' ),
    path('<int:pk>/', chat_people, name='chat_people' ),

]