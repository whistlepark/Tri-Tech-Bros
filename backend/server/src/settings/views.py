from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from settings.models import UserSettings, CameraSettings
from django.contrib.auth.models import User
from settings.forms import UserSettingForm
from camera.models import IPCamera
import json
from camera import Camera_API
# from ..camera import Camera_API
# from ..camera.models import IPCamera
import logging
logger = logging.getLogger(__name__)
logging.basicConfig( level=logging.DEBUG)



@login_required
def settings(request):
    curr_user = User.objects.get(username=request.user)
    if(request.method == "POST"):
        form = UserSettingForm(request.POST,instance=UserSettings)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    settingObjs = UserSettings.objects.all()
    form = UserSettingForm(instance=UserSettings)
    cams = IPCamera.objects.filter(user_id=curr_user.id)
    logging.debug(cams)
    return render(request, 'settings.html', {'fields':settingObjs,'settingForm':form})


@login_required
def apply_settings(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    ip = request.matchdict.get('ip')
    dhcp = request.matchdict.get('dhcp')
    if ip:
        camera.change_ip(ip)
    if dhcp is not '':
        camera.set_dhcp(dhcp)
    settingObjs = UserSettings.objects.all()
    form = UserSettingForm(instance=UserSettings)
    return render(request, 'settings.html', {'fields':settingObjs,'settingForm':form})

@login_required
def ptz_up(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    camera.move_up()

@login_required
def ptz_down(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    camera.move_down()

@login_required
def ptz_left(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    camera.move_left()

@login_required
def ptz_right(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    camera.move_right()

@login_required
def set_focus(request, ip):
    # camObj = IPCamera.objects.get(pk=pk)
    # camera = Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
    camera = Camera_API(ip, 86, 'admin', 'TriTechBr0s')
    focus = request.matchdict.get('focus')
    camera.set_focus(focus)



