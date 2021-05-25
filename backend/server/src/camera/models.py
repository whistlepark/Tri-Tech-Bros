from django.db import models

class IPCamera(models.Model):
    IP = models.CharField(max_length=20)
    streamURL = models.URLField(max_length=500)
    location = models.CharField(max_length=30)

