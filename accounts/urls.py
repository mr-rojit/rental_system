from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, upload_certificate


urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout_view"),
    path('profile/', profile_view, name="profile"),
    path('upload-certificate/', upload_certificate, name="upload-certificate"),
]