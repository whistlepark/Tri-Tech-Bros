from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class UserSettings(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    Always_Record = models.BooleanField(default=False)

class CameraSettings(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
