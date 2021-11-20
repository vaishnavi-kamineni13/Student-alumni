from django.db import models

# Create your models here.

class Request(models.Model):
    seller_username=models.CharField(max_length=10)
    buyer_username= models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')
    product_title=models.CharField(max_length=100)
    category=models.CharField(max_length=15)

class Orders(models.Model):
    seller_username=models.CharField(max_length=10)
    buyer_username= models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')
    product_title=models.CharField(max_length=100)
    category=models.CharField(max_length=15)
    