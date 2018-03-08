#coding: utf-8

from django import forms
from lawyer.models import LawyerModel



class LawyerForm(forms.ModelForm):

    class Meta:
        model = LawyerModel
        exclude = ['description']
        fields = '__all__'