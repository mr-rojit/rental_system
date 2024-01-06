from django.shortcuts import render
from django.views import View

class PostView(View):

    def get(self, request):
        return render(request, 'posts/posts-list.html')  
