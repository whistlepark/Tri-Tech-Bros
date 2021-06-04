from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class UserSettings(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    key = models.TextField(max_length=20)
    value = models.BooleanField()

class CameraSettings(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
