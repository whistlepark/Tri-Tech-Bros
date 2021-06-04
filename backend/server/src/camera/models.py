from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

class IPCamera(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    IP = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    record = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

