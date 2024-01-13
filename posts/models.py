from django.db import models

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
    title = models.CharField(max_length=100)
    description = models.TextField()
    property_area = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    location_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title




