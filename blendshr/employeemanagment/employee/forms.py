from django import forms
from django.db import models
from .models import employeeP
from moderator.choices import *
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from datetime import datetime, time, date, timedelta

min_date = date.today()
max_date = date.today() + timedelta(1 * 31)


class employee_profile(forms.ModelForm):
    maritial_status = forms.ChoiceField(choices=maritial_status, widget=forms.RadioSelect, required=True)
    gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect, required=True)

    class Meta:
        model = employeeP
        fields = '__all__'
        exclude = ['user', 'is_active']

