from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('signup_login', views.signup_login, name='signup_login'),
  path('signup', views.signup, name='signup'),
  path('login', views.login, name='login'),
  path('index', views.index, name='index'),
  path('profile/<int:user_id>', views.profile, name='profile'),
  # path('profile/<int:user_id>/<int:city_id>/update', views.update_profile, name='update_profile'),

]