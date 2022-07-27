from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from users.models import Profile

User = get_user_model()


class Colors(models.Model):

    color = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = ResizedImageField(size=[500, 500], crop=['middle', 'center'], quality=99,
                              blank=True, null=True, upload_to='images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Thing(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    temperature = models.IntegerField(null=False, blank=False)
    condition = models.IntegerField(default=1, null=True)
    mass = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    photo = ResizedImageField(size=[500, 500], crop=['middle', 'center'], quality=99,
                              blank=True, null=True, upload_to='images')