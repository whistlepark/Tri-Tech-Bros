from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from settings.models import UserSettings, CameraSettings
from django.contrib.auth.models import User
from settings.forms import UserSettingForm
from camera.models import IPCamera
import json
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


    return render(request, 'settings.html', {'cams':cams,'fields':settingObjs,'settingForm':form})
