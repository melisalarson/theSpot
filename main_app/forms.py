from django import forms
from .models import City, Post, User

class UserForm (forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name','city',] #we still need date