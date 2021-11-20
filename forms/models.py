from django.db import models

category_choices=[
    ('books','Books'),
    ('electronics','Electronics'),
    ('stationery','Stationery'),
    ('sports','Sports'),
    ('others','Others')
]

# Create your models here.
class Sellform(models.Model):
    username=models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    category=models.CharField(max_length=15, choices=category_choices)
    product_title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')
class Eventform(models.Model):
    username=models.CharField(max_length=10)
    event_name=models.CharField(max_length=100)
    start_date=models.CharField(max_length=25)
    end_date=models.CharField(max_length=25)
    link=models.CharField(max_length=1000)
    number=models.CharField(max_length=20)
    description=models.TextField()
    venue=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
class Clubs(models.Model):
    rollnumber=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    club_name=models.CharField(max_length=100)
