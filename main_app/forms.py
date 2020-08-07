from django import forms
from .models import City, Post, Profile

class ProfileForm (forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    # fields = ['profile_name', 'city', 'profile_picture']

class UserForm (forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    # fields = []

class CityForm (forms.ModelForm):
  class Meta:
    model = City
    fields = '__all__'
    fields = ['name', 'country', 'picture']

class PostForm (forms.ModelForm):
  class Meta:
    model = Post
    # fields = '__all__'
    fields = ['title', 'description', 'picture']
