from django import forms
from .models import City, Post, Profile

class ProfileForm (forms.ModelForm):
  class Meta:
    model = Profile
    # fields = '__all__'
    fields = ['city', 'user', 'profile_picture']

class UserForm (forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    # fields = []