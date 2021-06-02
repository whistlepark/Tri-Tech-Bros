from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from camera.models import IPCamera
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest, HttpResponse, StreamingHttpResponse,HttpResponsePermanentRedirect
from camera import camera
import json

@login_required
def devices(request,device_num=0):
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    form = IPCameraForm()
    cams = IPCamera.objects.all()

    return render(request,'devices.html',context={'cams':cams,'form':form})

@login_required
def video_feed(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    #return HttpResponse(json.dumps({'IP':camObj.IP,'Location':camObj.location}))
    return StreamingHttpResponse(camera.start_thread(pk),content_type='multipart/x-mixed-replace; boundary=frame')

@login_required
def record(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    camObj.record = not camObj.record
    camObj.save()
    return HttpResponsePermanentRedirect('/devices')
    return HttpResponse(camera.gen_frames(pk,record=True), mimetype='multipart/x-mixed-replace; boundary=frame')

@login_required
def stop_record(request, pk):
    camera.stop_record(pk)
    return HttpResponse()

@login_required
def remove(request,pk):
    if(request.method == "POST"):
        camera.stop_thread(pk)
        IPCamera.objects.filter(pk=pk).delete()
    return HttpResponsePermanentRedirect('/devices')

@login_required
def featured(request,pk):
    if(request.method == "POST"):
        camObj = IPCamera.objects.get(pk=pk)
        camObj.featured = not camObj.featured
        camObj.save()
    return HttpResponsePermanentRedirect('/devices')


