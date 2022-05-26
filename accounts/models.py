from django.db import models

# Create your models here.

class Signupstudent(models.Model):
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    mobile_number=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Signupalumni(models.Model):
    full_name= models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    mobile_number=models.CharField(max_length=20)
    working = models.CharField(max_length=10)
    company_name= models.CharField(max_length=100)
    dateofjoining=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    worklocation=models.CharField(max_length=100)
    company_name1=models.CharField(max_length=100)
    company_name2=models.CharField(max_length=100)
    company_name3=models.CharField(max_length=100)
    password=models.CharField(max_length=30)

class Vnr(models.Model):
    rollnumber=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    
