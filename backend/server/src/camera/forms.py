from django.forms import ModelForm
from camera.models import IPCamera

class IPCameraForm(ModelForm):
    class Meta:
        model = IPCamera
        fields = ['IP','streamURL','location']
