from django.urls import path
from .views import PostView, PostCreateView, PostDetailView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostView.as_view(), name="post_list"),
    path('create/', login_required(PostCreateView.as_view()), name="post_create"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail")
]