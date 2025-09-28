from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)


class Restaurant(models.Model):
    name = models.CharField(max_length= 20)
    picture = models.URLField(max_length=200, default="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/27/d5/bb/74/lounge.jpg?w=900&h=500&s=1")
    cuisine = models.CharField(max_length= 200)
    rating = models.FloatField()

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name="items")
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    is_veg= models.BooleanField(default= True)  