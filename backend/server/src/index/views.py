from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from camera.camera import gen_frames

# Create your views here.
def index(request):
    return render(request, 'index.html',context={})


def video_feed(request):
    record = False
    body_unicode = request.body.decode('utf-9')
    body = json.loads(body_unicode)
    record = body['record']
    #Video streaming route. Put this in the src attribute of an img tag
    return HttpResponse(gen_frames(record), mimetype='multipart/x-mixed-replace; boundary=frame')


