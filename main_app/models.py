from django.db import models
from django.contrib.auth.models import User
from datetime import date, timezone
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your models here.

image_storage = FileSystemStorage(
    # Physical file location ROOT
  location=u'{0}/uploads/'.format(settings.MEDIA_ROOT),
    # Url for file
  base_url=u'{0}uploads/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
  return u'picture/{0}'.format(filename)



class City(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=150)
  # picture = models.FileField(upload_to='uploads/')
  upload_picture = models.ImageField(upload_to='uploads/', storage=image_storage, null=True, blank=True)
      
  def __str__(self):
    return self.name
    
class Profile(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  profile_name = models.CharField(max_length=100)
  # city = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # profile_picture = models.FileField(upload_to='uploads/')
  upload_picture = models.ImageField(upload_to='uploads/', storage=image_storage, null=True, blank=True)
  def __str__(self):
    return self.profile_name

class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  # picture = models.FileField(upload_to='uploads/')
  upload_picture = models.ImageField(upload_to='uploads/', storage=image_storage, null=True, blank=True)
  date = models.DateField(auto_now=True)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
