from django.shortcuts import render
from django.views import View

class PostView(View):

    def get(self, request):
        return render(request, 'posts/posts-list.html')
    

class PostCreateView(View):

    def get(self,request):
        return render(request, 'posts/posts-create.html')
    
    def post(self,request):
        print(request.POST)
        return render(request, 'posts/posts-create.html')
