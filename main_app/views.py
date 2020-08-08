from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City, Post, Profile, User
from .forms import ProfileForm, UserForm, CityForm, PostForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import date, timezone, datetime




# Create your views here.

def home (request):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  return render(request, 'home.html', {'signup_form' : signup_form, 'form':form})

def cities (request):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  cities = City.objects.all()
  print(cities[0].__dict__)
  return render(request, 'cities.html', {'cities': cities, 'signup_form' : signup_form, 'form':form})
  
def city_index (request, city_id):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  post_form = PostForm()
  city = City.objects.get(id=city_id)
  posts = Post.objects.filter(city=city).order_by('-date')
  # print(posts.__dict__)
  context = {
    'city': city,
    'posts': posts,
    'signup_form' : signup_form,
    'form':form,
    'post_form': post_form,
    }
  return render(request, 'city_index.html', context)

def posts (request):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  posts = Post.objects.all()
  post_form = PostForm()
  return render(request, 'posts.html', {'posts': posts, 'signup_form' : signup_form, 'form':form, 'post_form': post_form})

def post_index (request, post_id):
  signup_form = UserCreationForm()
  form = AuthenticationForm()
  post = Post.objects.get(id=post_id)
  print(post)
  return render(request, 'post_index.html', {'post': post, 'signup_form': signup_form, 'form':form})

@login_required
def new_post(request):
  profile = Profile.objects.get(user=request.user)
  if request.method == 'POST':
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      new_post = post_form.save(commit=False)
      new_post.profile_id = profile.id
      new_post.save()
      return redirect('city_index', new_post.city_id)
      # if:
      #   return redirect('city_index', new_post.city_id)
      # else:  
      #   return redirect('posts')
    else:
      return HttpResponse('invalid input, go back on your browser and try again')
  else:
    post_form = PostForm()
    # post_form.profile = Profile.objects.get(user=request.user)
    return render(request, 'new_post.html', {'post_form': post_form,})

@login_required
def edit_post(request, post_id):
  # profile = Profile.objects.get(user=request.user)
  post = Post.objects.get(id=post_id)
  print(post.__dict__)
  if request.method == 'POST':
    edit_form = PostForm(request.POST, instance=post)
    if edit_form.is_valid():
      print('******')
      edited_post = edit_form.save()
      # edited_post.profile_id = profile.id
      # edited_post.save()
      return redirect('city_index', post.city_id)
    else:
      return HttpResponse('invalid input, go back on your browser and try again')
  else:
    edit_form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'edit_form': edit_form, 'post' : post})

@login_required
def delete_post(request, post_id):
  post = Post.objects.get(id=post_id)
  city_id = post.city_id
  post.delete()
  return redirect('city_index', city_id)





def upload(request, context):
  if request.method == 'POST':
    uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    context['url'] = fs.url(name)
    print(profile.default_picture)
  return render(request, 'profile.html', context)

def signup (request):
  error = ''
  form = UserCreationForm()
  city = City.objects.all().first()
  picture = 'media/default_picture.png'
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
  posts = Post.objects.filter(profile=profile).order_by('date')
  context = {
    'profile': profile,
    'profile_form': profile_form,
    'posts': posts,
  }
  print(profile.default_picture)
  return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
  profile = Profile.objects.get(user=request.user)
  # cities = City.objects.all()
  # posts = Post.objects.all()
  context = {'profile': profile}
  if request.method == 'POST':
    profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
    if profile_form.is_valid():
      profile_form.save()
      context['profile_form'] = profile_form
      context['city'] = profile.city
      print(profile.default_picture)
      # return redirect('upload', context)
      return redirect('profile')
    else:
      return HttpResponse('invalid input, go back on your browser and try again')
  else:
    profile_form = ProfileForm(instance=profile)
    context['profile_form'] = profile_form
    # context['city'] = profile.city
    # return redirect('upload', context)
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

