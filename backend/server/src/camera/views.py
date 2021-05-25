from django.shortcuts import render
from camera.models import IPCamera
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest

def devices(request):
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
    else:
        form = IPCameraForm()
        cams = IPCamera.objects.all()

    return render(request,'devices.html',context={'cams':cams,'form':form})
