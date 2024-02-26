from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('rent', 'Rent'),
        ('sale', 'Sale'),
        ('lease', 'Lease'),

    )
    category_name = models.CharField(max_length=5, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    property_area = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    location_name = models.CharField(max_length=100)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    bathroom = models.IntegerField(default=1)
    bedroom = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f'Image of post {self.post.pk}'




