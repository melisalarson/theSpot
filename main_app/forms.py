from django import forms
from .models import City, Post, Profile

class ProfileForm (forms.ModelForm):
  class Meta:
    model = Profile
    # fields = '__all__' #we still need date
    fields = ['city',]