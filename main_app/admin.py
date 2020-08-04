from django.contrib import admin

# Register your models here.
from .models import City, Post, User
admin.site.register(City)
admin.site.register(Post)
admin.site.register(User)