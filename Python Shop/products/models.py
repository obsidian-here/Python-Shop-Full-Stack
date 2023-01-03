from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255) #a character field with max length
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083) #thats the standard maximum length of urls
    
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()