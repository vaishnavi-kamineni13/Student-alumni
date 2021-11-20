from django.db import models

# Create your models here.

class Signup(models.Model):
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    mobile_number=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
class Vnr(models.Model):
    rollnumber=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    
