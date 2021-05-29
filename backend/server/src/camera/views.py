from django.shortcuts import render
from camera.models import IPCamera
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest, HttpResponse
from camera import camera

def devices(request,device_num=0):
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    form = IPCameraForm()
    cams = IPCamera.objects.all()

    return render(request,'devices.html',context={'cams':cams,'form':form})

def record():
    #Video streaming route. Put this in the src attribute of an img tag
    return HttpResponse(camera.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
