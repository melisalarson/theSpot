from django import forms
from .models import City, Post, User

class UserForm (forms.ModelForm):
  class Meta:
    model = User
    # fields = '__all__' #we still need date
    fields = ['first_name', 'city',]