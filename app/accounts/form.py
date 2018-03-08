#coding: utf-8

from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User



class UserForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=30)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if (password1 and password2) and (password1 != password2):
            raise forms.ValidationError('senhas incorretas, verifique os campos.')
        return password2

    def save(self, commit=True):
        user_obj = User(
            is_staff=False,
            is_superuser=False,
            username=self.cleaned_data.get("username"),
        )
        user_obj.password = make_password(password=self.cleaned_data.get("password1"),
                                            salt=None, hasher='default')

        if commit:
            user_obj.save()
        return user_obj
