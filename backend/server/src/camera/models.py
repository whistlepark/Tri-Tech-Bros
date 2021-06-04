from django.db import models

class IPCamera(models.Model):
    IP = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    record = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)



