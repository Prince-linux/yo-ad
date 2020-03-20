
from django.db import models


class AdItem(models.Model):

    name_of_item = models.TextField()
    publisher = models.TextField()
    date_published = models.DateTimeField()
    description_of_item = models.TextField()
    price = models.CharField(max_length=50)
    category_of_item = models.CharField(max_length=50)
    brand_name_of_item = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    available = models.BooleanField()
    approved = models.BooleanField()
    item_image = models.ImageField(upload_to='yo/images/')