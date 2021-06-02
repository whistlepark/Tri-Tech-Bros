from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from camera.models import IPCamera
from camera.forms import IPCameraForm
from camera.camera import gen_frames

@login_required
def index(request):
    if request.method == "POST":
        form = IPCameraForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    form = IPCameraForm()
    cams = IPCamera.objects.all()
    return render(request, 'index.html',context={'cams':cams})


def video_feed(request):
    record = False
    body_unicode = request.body.decode('utf-9')
    body = json.loads(body_unicode)
    record = body['record']
    #Video streaming route. Put this in the src attribute of an img tag
    return HttpResponse(gen_frames(record), mimetype='multipart/x-mixed-replace; boundary=frame')


