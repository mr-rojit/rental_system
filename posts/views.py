from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Post, PostImage
from django.db.models import Q
class PostView(View):

    def get(self, request):
        queryset = Post.objects.all()
        keyword = self.request.GET.get('keyword')
        city = self.request.GET.get('city')
        cat = self.request.GET.get('cat')
        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(title__icontains=keyword))
        if city:
            queryset = queryset.filter(city__icontains=city)
        return render(request, 'posts/posts-list.html', {'posts': queryset})
    
class PostDetailView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/posts-detail.html', {'post': post})

class PostCreateView(View):

    def get(self,request):
        return render(request, 'posts/posts-create.html')
    
    def post(self,request):
        category = request.POST.get('category', '')
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        district = request.POST.get('district', '')
        city = request.POST.get('city', '')
        location = request.POST.get('location-name', '')
        price = float(request.POST.get('price', ''))

        cat = Category.objects.get(category_name__iexact=category)
        post = Post.objects.create(category=cat, title=title, description=description,
                             district=district, property_area='', city =city, location_name=location,
                             price=price, user=request.user
                             )
        
        img1 = request.FILES.get('image1', '')
        img2 = request.FILES.get('image2', '')
        img3 = request.FILES.get('image3', '')
        img4 = request.FILES.get('image4', '')

        PostImage.objects.create(post=post, picture=img1)
        PostImage.objects.create(post=post,picture=img2)
        PostImage.objects.create(post=post,picture=img3)
        PostImage.objects.create(post=post,picture=img4)

        print(request.FILES)
        return render(request, 'posts/posts-create.html')
