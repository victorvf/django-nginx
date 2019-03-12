from django import forms
from . import models

class PeopleForm(forms.ModelForm):
    class Meta:
        model = models.People
        fields = '__all__'

class RotaryForm(forms.ModelForm):
    class Meta:
        model = models.Rotary
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = '__all__'

class MonthlyForm(forms.ModelForm):
    class Meta:
        model = models.Monthly
        fields = '__all__'
