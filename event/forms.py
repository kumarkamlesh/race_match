from django.forms import ModelForm

from . import models


class PresetListForm(ModelForm):
    class Meta:
        model = models.WinnerPlayer
