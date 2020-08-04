from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    picture = models.FileField(upload_to='uploads/')

class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    picture = models.FileField(upload_to='uploads/')
    date = models.DateField()
    