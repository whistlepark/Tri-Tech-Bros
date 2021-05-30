from django.db import models

class SettingField(models.Model):
    key = models.TextField(max_length=20)
    value = models.BooleanField()

