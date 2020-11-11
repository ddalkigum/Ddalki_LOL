from django import forms
from . import models


class TipCreateForm(forms.ModelForm):
    class Meta:
        model = models.Tip
        fields = ("description",)
