from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City, Post, Profile, User
from .forms import ProfileForm, UserForm, CityForm, PostForm
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
  posts = Post.objects.filter(city=city).order_by('-date')
  context = {
    'city': city,
    'posts': posts,
    }
  return render(request, 'city_index.html', context)

def posts (request):
  posts = Post.objects.all()
  print(posts[0])
  return render(request, 'posts.html', {'posts': posts})

def post_index (request, post_id):
  post = Post.objects.get(id=post_id)
  print(post)
  return render(request, 'post_index.html', {'post': post})

def signup (request):
  error = ''
  form = UserCreationForm()
  city = City.objects.all().first()
  print(city)
  picture = 'media/uploads/continents-28616_960_720.png'
  context = {
    'form': form,
    'error': error,
    'city': city,
  }
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user)
      profile_user = Profile(user=user, profile_name=user.username, city=city, profile_picture=picture)
      profile_user.save()
      return redirect('profile')
    else:
      return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
  else:
    return render(request, 'registration/signup.html', context)


@login_required
def profile (request):
  profile = Profile.objects.get(user=request.user)
  profile_form = ProfileForm(instance=profile)
  posts = Post.objects.filter(profile=profile).order_by('-date')
  context = {
    'profile': profile,
    'profile_form': profile_form,
    'posts': posts,
  }
  return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
  profile = Profile.objects.get(user=request.user)
  # cities = City.objects.all()
  # posts = Post.objects.all()
  context = {'profile': profile}
  if request.method == 'POST':
    profile_form = ProfileForm(request.POST, instance=profile)
    if profile_form.is_valid():
      profile_form.save()
      return redirect('profile')
    else:
      return HttpResponse('invalid input, go back on your browser and try again')
  else:
    profile_form = ProfileForm(instance=profile)
    context['profile_form'] = profile_form
    return render(request, 'edit_profile.html', context)


# # @login_required
# # def profile (request): # this one should be edit profile?
#   # profile = Profile.objects.get(user=request.user)
#   # profile = Profile.objects.all()
#   profile = Profile.objects.get(user=request.user)
#   # user = profile.user
#   # users = User.objects.filter(city_id=User['city_id'])
  
#   # first_name = Profile.objects.get(user=request.user).first_name
#   # print(users)
#   # posts = Post.objects.get(profile)
#   # post = posts.title
#   city = profile.city.name
#   # city = City.objects.get(profile.city_id)
#   # join_date = User.objects.get(request.date_joined)
#   # user = User.objects.get(id=user_id)
#   print('**************this is profile')
#   # print(profile)
#   # print(city)
#   # print(posts)

#   profile_form = ProfileForm(instance=profile)

#   print('**************this is form')
#   # print(profile_form)
#   context = {
#     'profile': profile,
#     'city': city,
#     'profile_form': profile_form,
#     'posts': posts,
#     # 'user': user
#     # 'first_name': first_name
#   }
#   return render(request, 'profile.html', context)

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
