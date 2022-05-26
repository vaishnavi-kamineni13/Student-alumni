from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Analysis(models.Model):
    question=models.TextField()
    answer=models.TextField()
    companyname=models.CharField(max_length=100)
    usernameans= models.CharField(max_length=10)