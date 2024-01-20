from django.urls import path
from .views import PostView, PostCreateView, PostDetailView

urlpatterns = [
    path('', PostView.as_view(), name="post_list"),
    path('create/', PostCreateView.as_view(), name="post_create"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail")
]