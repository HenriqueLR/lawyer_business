#coding: utf-8

from django import forms
from business.models import BusinessModel



class BusinessForm(forms.ModelForm):

    class Meta:
        model = BusinessModel
        fields = '__all__'