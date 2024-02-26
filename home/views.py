from django.shortcuts import render
from posts.models import Post

def home_page(request):
    recent = Post.objects.all().order_by('-id')[:3]
    return render(request, 'home/home.html', {'recent': recent})
