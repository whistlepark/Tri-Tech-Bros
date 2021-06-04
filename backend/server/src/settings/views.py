from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from settings.models import SettingField
from settings.forms import SettingForm
import json
# from ..camera import Camera_API
# from ..camera.models import IPCamera

@login_required
def settings(request):
    if(request.method == "POST"):
        form = SettingForm(request.POST,instance=SettingField)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    settingObjs = SettingField.objects.all()
    form = SettingForm(instance=SettingField)

    return render(request, 'settings.html', {'fields':settingObjs,'settingForm':form})


@login_required
def ptz_up(request, ip):
    camObj = IPCamera.objects.get(pk=pk)
    Camera_API(camObj.host, camObj.port, camObj.user, camObj.password)
