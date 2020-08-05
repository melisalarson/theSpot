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
  user = User.objects.get(id=user_id)
  city = City.objects.get(user.city_id)
  print(user)
  form = UserForm(user)
  print(form)
  context = {
    'user': user,
    'form': form,
    'city': city, 
  }
  return render(request, 'profile.html', context)

def update_profile (request, user_id, city_id):
  user = User.objects.get(id=user_id)
  city = City.objects.get(id=city_id)
  
  if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
              user = form.save()
              return redirect('profile', user.id)
  else:
        form = UserForm(instance=user)
        return render(request, 'update_profile.html', { 'form': form })
        
  # print(form)
  # context = {
  #   'user': user,
  #   'form': form,
  #   'city': city, 
  # }

def index (request):
      return render(request, 'index.html')
