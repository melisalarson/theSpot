from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Post, Profile
from .forms import ProfileForm

# Create your views here.

def home (request):
  return render(request, 'home.html')

# option A sign up and login together
def signup_login (request):
  return render(request, 'signupLogin.html')

  # option B sign up and login separate
def signup (request):
  # User - get it using userForm
  # user.save as post => creates user
  # with this user object get user id and create a profile


  return render(request, 'signup.html')

def login (request):
  return render(request, 'login.html')

def profile (request, user_id):
  user = Profile.objects.get(id=user_id).__dict__
  city = City.objects.get(user.city_id).__dict__

  print('this is my user ...')
  print(user)
  print('this is my city ...')
  print(city)
  form = ProfileForm(user)
  print(form)
  context = {
    'user': user,
    'form': form,
    'city': city,
  }
  return render(request, 'profile.html', context)

def index (request):
      return render(request, 'index.html')
