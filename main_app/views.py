from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City, Post, Profile, User
from .forms import ProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home (request):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  return render(request, 'home.html', {'signup_form' : signup_form, 'form':form})

def cities (request):
  cities = City.objects.all()
  print(cities[0].__dict__)
  return render(request, 'cities.html', {'cities': cities})
  
def city_index (request, city_id):
  city = City.objects.get(id=city_id)
  print(cities)
  return render(request, 'city_index.html', {'city': city})

def posts (request):
  posts = Post.objects.all()
  print(posts[0])
  return render(request, 'posts.html', {'posts': posts})

def post_index (request, post_id):
  post = Post.objects.get(id=post_id)
  print(post)
  return render(request, 'post_index.html', {'post': post})




@login_required
def profile (request): # this one should be edit profile?
  # profile = Profile.objects.get(user=request.user)
  # profile = Profile.objects.all()
  profile = Profile.objects.get(user=request.user)
  # user = profile.user
  # users = User.objects.filter(city_id=User['city_id'])
  
  # first_name = Profile.objects.get(user=request.user).first_name
  # print(users)
  # posts = Post.objects.get(profile)
  # post = posts.title
  city = profile.city.name
  # city = City.objects.get(profile.city_id)
  # join_date = User.objects.get(request.date_joined)
  # user = User.objects.get(id=user_id)
  print('**************this is profile')
  print(profile)
  # print(city)
  # print(posts)

  profile_form = ProfileForm(instance=profile)

  print('**************this is form')
  # print(profile_form)
  context = {
    'profile': profile,
    'city': city,
    'profile_form': profile_form,
    'posts': posts,
    # 'user': user
    # 'first_name': first_name
  }
  return render(request, 'profile.html', context)
  # return HttpResponse('hello')

def signup (request):
  error = ''
  form = UserCreationForm()
  context = {
    'form': form,
    'error': error,
  }
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      return redirect('profile')
    else:
      return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
      # error_message = 'Invalid credentials - please try again'
  else:
    return render(request, 'registration/signup.html', context)


# @login_required
# def profile (request):
#   # profile = Profile.objects.get(user=request.user)
#   profile = Profile.objects.get(user=request.user).__dict__
#   # city = Profile.objects.get(profile.city)
#   # user = City.objects.get(profile.user)
#   print(profile)
#   # print(city)
#   # print(posts)

#   form = ProfileForm(profile)
#   print(form)
#   context = {
#     'profile': profile,
#     # 'city': city,
#     'form': form,
#   }
#   return render(request, 'profile.html', context)
#   # return HttpResponse('hello')

# @login_required
# def posts_index(request):
#   posts = Post.objects.filter(user=request.user)
#   return render(request, 'posts/index.html', { 'posts': posts })

# @login_required
# def new_post(request):
#   if request.method == 'POST':
#       form = PostForm(request.POST)
#       if form.is_valid():
#           post = form.save(commit=False)
#           post.user = request.user
#           post.save()
#           return redirect('profile', post.id)
#   else:
#       form = PostForm()
#   context = { 'form': form }
#   return render(request, 'posts/post_form.html', context)
