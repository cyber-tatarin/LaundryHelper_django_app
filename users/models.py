from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)


class User(AbstractUser):
    email = models.EmailField(null=True, blank=False, unique=True)
    profiles = models.ManyToManyField(Profile, blank=False)
