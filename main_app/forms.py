from django import forms
from .models import City, Post, Profile

class ProfileForm (forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_name', 'city','upload_picture']

class UserForm (forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'

class CityForm (forms.ModelForm):
  class Meta:
    model = City
    fields = ['name', 'country']

class PostForm (forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'description', 'city', 'upload_picture']
