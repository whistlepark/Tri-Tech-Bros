from django.shortcuts import render
from django.http import HttpResponse
from settings.models import SettingField
from settings.forms import SettingForm
import json

def settings(request):
    if(request.method == "POST"):
        form = SettingForm(request.POST,instance=SettingField)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.save()

    settingObjs = SettingField.objects.all()
    form = SettingForm(instance=SettingField)

    return render(request, 'settings.html', {'fields':settingObjs,'settingForm':form})
