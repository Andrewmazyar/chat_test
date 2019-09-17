from django.contrib import admin
from .models import Profile, Chat

# Register your models here.

admin.site.register(Chat)
admin.site.register(Profile)