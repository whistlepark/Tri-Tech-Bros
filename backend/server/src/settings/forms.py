from django.forms import ModelForm, BooleanField
from settings.models import SettingField

class SettingForm(ModelForm):
    value = BooleanField()

    class Meta:
        model = SettingField
        fields = ('key','value',)
        # exclude = ('key',)
        
