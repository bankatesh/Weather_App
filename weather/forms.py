from django import forms
from django.forms import ModelForm

from .models import *

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
