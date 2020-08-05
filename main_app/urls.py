from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('signup_login', views.signup_login, name='signup_login'),
  path('signup', views.signup, name='signup'),
  path('loginn', views.loginn, name='loginn'),

  path('profile/<int:user_id>', views.profile, name='profile'),

]