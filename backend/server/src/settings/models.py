from django.db import models
from camera.models import IPCamera

class SettingField(models.Model):
    key = models.TextField(max_length=20)
    value = models.BooleanField()
    camera = models.ForeignKey(to=IPCamera, on_delete=models.CASCADE)
