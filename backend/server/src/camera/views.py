from django.shortcuts import render
from camera.models import IPCamera
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest, HttpResponse, StreamingHttpResponse,HttpResponsePermanentRedirect
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
    return StreamingHttpResponse(camera.start_thread(pk),content_type='multipart/x-mixed-replace; boundary=frame')

def record(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    return HttpResponse(camera.start_record(pk), mimetype='multipart/x-mixed-replace; boundary=frame')

def stop_record(request, pk):
    camera.stop_record(pk)
    return HttpResponse()

def remove(request,pk):
    if(request.method == "POST"):
        camera.stop_thread(pk)
        IPCamera.objects.filter(pk=pk).delete()
    return HttpResponsePermanentRedirect('/devices')

