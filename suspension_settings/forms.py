from django import forms

from .models import Setting

class SettingForm(forms.ModelForm):

    class Meta:
        model = Setting
        fields = ('Bike', 'SpringRate', 'FrontCompression', 'FrontRebound', 'RearHighSpeedCompression',
              'RearLowSpeedCompression', 'RearRebound', 'Sag', 'Notes',
                )
        widgets = {'Bike': forms.HiddenInput()}