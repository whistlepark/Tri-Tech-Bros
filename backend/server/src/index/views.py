from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from camera.camera import gen, VideoCamera

# Create your views here.
def index(request):
    return render(request, 'index.html',context={})


def videoFeed(request):
    return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')
