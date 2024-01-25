from django.shortcuts import render

def chat_home(request):
    return render(request, 'chat/chat_home.html')
