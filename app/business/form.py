#coding: utf-8

from django import forms
from business.models import BusinessModel



class BusinessForm(forms.ModelForm):

    def save(self, user=None, commit=True):
        business = super(BusinessForm, self).save(commit=False)
        business.user = user

        if commit:
            business.save()
        return business

    class Meta:
        model = BusinessModel
        exclude = ['user']
        fields = '__all__'