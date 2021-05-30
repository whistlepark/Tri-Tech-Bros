from django.shortcuts import render
from camera.models import IPCamera
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest, HttpResponse, StreamingHttpResponse
from camera import camera
import json

def devices(request,device_num=0):
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    form = IPCameraForm()
    cams = IPCamera.objects.all()

    return render(request,'devices.html',context={'cams':cams,'form':form})

def video_feed(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    #return HttpResponse(json.dumps({'IP':camObj.IP,'Location':camObj.location}))
    return StreamingHttpResponse(camera.gen_frames(pk),content_type='multipart/x-mixed-replace; boundary=frame')

def record(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    return HttpResponse(camera.gen_frames(pk,record=True), mimetype='multipart/x-mixed-replace; boundary=frame')
