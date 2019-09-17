from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)


class Chat(models.Model):
    description = models.TextField(
        verbose_name='поле для користувача',
    )
    profile = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)