from django.forms import ModelForm, BooleanField
from settings.models import UserSettings, CameraSettings

class UserSettingForm(ModelForm):
    value = BooleanField()

    class Meta:
        model = UserSettings
        fields = ('key','value',)
        # exclude = ('key',)
        
