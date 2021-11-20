from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')
class Electronics(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='media/pics')
class Stationery(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='media/pics')
class Sports(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='media/pics')
class Others(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='media/pics')
class Favourites(models.Model):
    username=models.CharField(max_length=10)
    favourite_username=models.CharField(max_length=10)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='media/pics')
    category=models.CharField(max_length=15)
