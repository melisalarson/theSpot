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
  return render(request, 'signup.html')

def loginn (request):
  return render(request, 'loginn.html')

def profile (request, user_id):
  user = User.objects.get(id=user_id).__dict__
  print(user)
  form = UserForm(user)
  print(form)
  context = {
    'user': user,
    'form': form,
  }
  return render(request, 'profile.html', context)

# def update (request):

#   return render(request, 'profile.html')

def index (request):
      return render(request, 'index.html')
