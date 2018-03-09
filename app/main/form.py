#coding: utf-8

from django import forms
from main.models import OrderServiceModel, BusinessLawyerModel



class OrderServiceForm(forms.ModelForm):

    class Meta:
        model = OrderServiceModel
        exclude = ['business']
        fields = '__all__'



class BusinessLawyerForm(forms.ModelForm):

    class Meta:
        model = BusinessLawyerModel
        exclude = ['status', 'lawyer']
        fields = '__all__'