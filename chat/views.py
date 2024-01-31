from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Chat

User = get_user_model()

def chat_home(request):
    return render(request, 'chat/chat_home.html')

def chat_people(request, pk):
    this_user = request.user
    other_user = User.objects.get(pk=pk)
    messages =Chat.objects.filter(message_from=this_user, message_to=other_user)

    return render(request, 'chat/chat_home.html')