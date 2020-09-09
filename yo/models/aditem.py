
from django.db import models

# CATEGORY = [
#     ('Business & Industry', 'BUSINESS $ INDUSTRY'),
#     ('Clothing & Beauty', 'CLOTHING & BEAUTY'),
#     ('Agriculture', 'AGRICULTURE'),
#     ('Electronics', 'ELECTRONICS'),
#     ('Essentials', 'ESSENTIALS'),
#     ('Hobby, Sports & Kids', 'HOBBY, SPORTS & KIDS'),
#     ('Real Estate, Home & Garden', 'REAL ESTATE, HOME & GARDEN'),
#     ('Jobs in Ghana', 'JOBS IN GHANA'),
#     ('Foreign Jobs', 'FOREIGN JOBS'),
#     ('Other', 'OTHER',),
#     ('Pets & Animals', 'PETS & ANIMALS'),
#     ('Property', 'PROPERTY'),
#     ('Services', 'SERVICES'),
#     ('Vehicles', 'VEHICLES')
# ]

class AdItem(models.Model):
    name_of_item = models.TextField()
    publisher = models.TextField()
    date_published = models.DateTimeField()
    description_of_item = models.TextField()
    price = models.FloatField()
    brand_name_of_item = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    available = models.BooleanField()
    approved = models.BooleanField()
    promoted = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    item_image = models.ImageField(upload_to='yo/images/')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('AdItem', on_delete=models.CASCADE)



class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

# class PayPromotion(models.Model):
#     promotional_price = models.CharField(max_length=10)
#     promotion = models.OneToOneField('AdItem', on_delete=models.CASCADE)
#     #status = ['Promoted', 'Normal']





