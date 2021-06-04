from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

from camera.models import IPCamera
from camera.forms import IPCameraForm
from camera.camera import gen_frames

import json

@login_required
def index(request):
    curr_user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        new_cam = form.save(commit=False)
        new_cam.user_id = curr_user.id
        new_cam.save()
    form = IPCameraForm()
    cams = IPCamera.objects.filter(user_id=curr_user.id)
    return render(request, 'index.html',context={'cams':cams, 'user':request.user})

@login_required
def video_feed(request):
    record = False
    body_unicode = request.body.decode('utf-9')
    body = json.loads(body_unicode)
    record = body['record']
    #Video streaming route. Put this in the src attribute of an img tag
    return HttpResponse(gen_frames(record), mimetype='multipart/x-mixed-replace; boundary=frame')

@login_required
def user(request):
    return HttpResponse(User.objects.get(username=request.user).id)
    return HttpResponse(json.dumps(SocialAccount.objects.get(user=request.user).extra_data))#objects.all())
    return HttpResponse({'user':User.objects.get(username=request.user.username)})

