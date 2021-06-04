from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from settings.models import UserSettings, CameraSettings
from settings.forms import UserSettingForm
import json

@login_required
def settings(request):
    if(request.method == "POST"):
        form = UserSettingForm(request.POST,instance=UserSettings)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    settingObjs = UserSettings.objects.all()
    form = UserSettingForm(instance=UserSettings)

    return render(request, 'settings.html', {'fields':settingObjs,'settingForm':form})
