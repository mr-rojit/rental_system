from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Chat, Channel
from django.utils import timezone

User = get_user_model()

def chat_home(request):
    channels = Channel.objects.filter(Q(user_one=request.user)|Q(user_two=request.user)).order_by('-updated_at')
    new_channels = []
    for c in channels:
        dict = {}
        dict['channel_id'] = c.pk
        if c.user_one == request.user:
            dict['other_user'] = c.user_two
        else:
            dict['other_user'] = c.user_one
        new_channels.append(dict)
    return render(request, 'chat/chat_home.html', {'channels': new_channels})


def get_or_create_channel(request, pk):
    other_user = User.objects.get(pk=pk)
    current_user = request.user
    c1 = Channel.objects.filter(user_one=current_user, user_two=other_user).exists()
    if not c1:
        c2 = Channel.objects.filter(user_one=other_user, user_two=current_user).exists()
        if not c2:
            c = Channel.objects.create(user_one=current_user, user_two=other_user)
            return redirect(chat_people, pk=c.pk)
        c2 = Channel.objects.filter(user_one=other_user, user_two=current_user).first()
        return redirect(chat_people, pk=c2.pk)
    c1 = Channel.objects.filter(user_one=current_user, user_two=other_user).first()
    return redirect(chat_people, pk=c1.pk)


def chat_people(request, pk):
    channel = Channel.objects.get(pk=pk)
    chats = Chat.objects.filter(channel=channel).order_by('created_at')
    channels = Channel.objects.filter(Q(user_one=request.user)|Q(user_two=request.user)).order_by('-updated_at')
    new_channels = []
    for c in channels:
        dict = {}
        dict['channel_id'] = c.pk
        if c.user_one == request.user:
            dict['other_user'] = c.user_two
        else:
            dict['other_user'] = c.user_one
        new_channels.append(dict)

    return render(request, 'chat/chat_home.html', {'channels': new_channels, 'chats': chats})

def send_chat(request):
    channel_id = request.POST.get('channel_id').split('/')[-2]
    channel = Channel.objects.get(pk=channel_id)
    if channel.user_one == request.user:
        msg_to = channel.user_two
    else:
        msg_to = channel.user_one
    msg = request.POST.get('message')
    Chat.objects.create(message=msg, channel=channel, message_from=request.user, message_to=msg_to)
    channel.updated_at = timezone.now()
    channel.save()
    return redirect(chat_people, pk=channel_id)