from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    picture = models.FileField(upload_to='uploads/')

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    picture = models.FileField(upload_to='uploads/')
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
