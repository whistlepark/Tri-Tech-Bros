
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from camera.models import IPCamera
from camera import Camera_API
from camera.forms import IPCameraForm
from django.http import HttpResponseBadRequest, HttpResponse, StreamingHttpResponse,HttpResponsePermanentRedirect
from camera import camera
import json

@login_required
def devices(request,device_num=0):
    curr_user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        new_cam = form.save(commit=False)
        new_cam.user_id = curr_user.id
        cam = new_cam.save()

        # # Setup Camera
        # if cam.ip == '192.168.1.108':
        #     cam.ip = ''
        # if cam.username == NULL:
        #     cam.username = 'admin'
        #     cam.password = 'TriTechBr0s'


    form = IPCameraForm()
    cams = IPCamera.objects.filter(user_id=curr_user.id)

    return render(request,'devices.html',context={'cams':cams,'form':form})

@login_required
def video_feed(request,pk):
    camObj = IPCamera.objects.get(pk=pk)
    #return HttpResponse(json.dumps({'IP':camObj.IP,'Location':camObj.location}))
    return StreamingHttpResponse(camera.gen_frames(pk),content_type='multipart/x-mixed-replace; boundary=frame')

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


