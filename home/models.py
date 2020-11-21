from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Home(models.Model):
    image= models.ImageField(default="" ,upload_to= "questions/")
    question= models.CharField(max_length=100,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=12,null=True)
    description = models.CharField(max_length=200, null=True)
    date = models.DateField()

class posts(models.Model):
    user_name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=20,null=True)
    Content = models.TextField(max_length=1000,null=True)
    date_posted = models.DateTimeField(default=timezone.now,null=True)

    