from django.db import models


class AdItem(models.Model):

    CATEGORY = (
        ('ELECTRONICS', 'electronics'),
        ('HOUSING & REAL ESTATES', 'housing & real estates'),
        ('FURNITURE', 'furniture'),
        ('FOOD', 'food'),
        ('CLOTHING', 'clothing'),
        ('VEHICLES & BIKES', 'vehicles & bikes'),
        ('BOOKS', 'books'),
    )

    BRAND_NAME = (
        ('HP', 'hp'),
        ('SAMSUNG', 'samsung'),
        ('APPLE', 'apple'),
        ('LG', 'lg'),
        ('TOSHIBA', 'toshiba'),
        ('LAND ROVER', 'land rover'),
        ('MERCEDES', 'mercedes'),
        ('OTHER', 'other'),
    )

    LOCATION = (
        ('ACCRA', 'accra'),
        ('KUMASI', 'kumasi'),
        ('TEMA', 'tema'),
        ('KOFORIDUA', 'koforidua'),
        ('TAKORADI', 'takoradi'),
        ('WINNEBA', 'winneba'),
        ('TAMALE', 'tamale'),
        ('WA', 'wa'),
        ('BOLGATANGA', 'bolgatanga'),
        ('SUNYANI', 'sunyani'),
        ('SEKONDI', 'sekondi'),
        ('CAPE-COAST', 'cape-coast'),
        ('HO', 'ho'),
    )

    name_of_item = models.TextField()
    publisher = models.TextField()
    date_published = models.DateTimeField()
    description_of_item = models.TextField()
    price = models.CharField(max_length=1)
    category_of_item = models.CharField(max_length=1, choices=CATEGORY)
    brand_name_of_item = models.CharField(max_length=1, choices=BRAND_NAME)
    location = models.CharField(max_length=1, choices=LOCATION)
    contact = models.CharField(max_length=1)
    available = models.BooleanField()
    approved = models.BooleanField()
    item_image = models.ImageField(upload_to='yo/images/')