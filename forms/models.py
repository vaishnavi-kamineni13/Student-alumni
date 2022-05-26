from pyexpat import model
from django.db import models

category_choices=[
    ('Amazon','Amazon'),
    ('JPMC','JPMC'),
    ('Deloitte','Deloitte'),
    ('TCS','TCS'),
    ('Infosys','Infosys'),
    ('Wipro','Wipro'),
    ('Accenture','Accenture'),
    ('LTI','LTI'),
    ('Atlassian','Atlassian'),
    ('NCR','NCR'),
    ('Cognizant','Cognizant'),
    ('Factset','Factset'),
    ('Capgemini','Capgemini'),
    ('ACS','ACS'),
    ('Accolite','Accolite'),
    ('F5','F5'),
    ('StateStreet','StateStreet'),
    ('DBS','DBS'),
    ('Others','Others')
]

# Create your models here.
class Questionform(models.Model):
    username=models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    companyname1=models.CharField(max_length=50, choices=category_choices)
    companyname2=models.CharField(max_length=100)
    question=models.TextField()

class Techform(models.Model):
    username=models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    question=models.TextField()

class Techansform(models.Model):
    username=models.CharField(max_length=10)
    student_username = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    question=models.CharField(max_length=500)
    answer=models.TextField()

class Answerform(models.Model):
    username=models.CharField(max_length=10)
    student_username = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    question=models.CharField(max_length=500)
    answer=models.TextField()

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

class Event(models.Model):
    rollnumber=models.CharField(max_length=10)
    full_name=models.CharField(max_length=100)
    department=models.CharField(max_length=200)
    mobile_number=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
