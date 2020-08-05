from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Post, User
from .forms import UserForm

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

def loginn (request):
  return render(request, 'loginn.html')

def profile (request, user_id, city_id):
  user = User.objects.get(id=user_id).__dict__
  city = City.objects.get(id=city_id).__dict__
  # city.id = user.city_id
  # user.city_id = city.id

  print('this is my user ...')
  print(user)
  print('this is my city ...')
  print(city)
  form = UserForm(user)
  print(form)
  context = {
    'user': user,
    'form': form,
    'city': city,
  }
  return render(request, 'profile.html', context)

def index (request):
      return render(request, 'index.html')
