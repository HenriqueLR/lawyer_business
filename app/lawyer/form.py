#coding: utf-8

from django import forms
from lawyer.models import LawyerModel



class LawyerForm(forms.ModelForm):

    def save(self, user=None, commit=True):
        lawyer = super(LawyerForm, self).save(commit=False)
        lawyer.user = user

        if commit:
            lawyer.save()
        return lawyer

    class Meta:
        model = LawyerModel
        exclude = ['description', 'user']
        fields = '__all__'
