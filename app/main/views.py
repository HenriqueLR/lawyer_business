#coding: utf-8

from django.shortcuts import render
from lawyer.form import LawyerForm



def home(request):
    context = {'form_lawyer':LawyerForm()}
    template_name = 'home.html'
    return render(request, template_name, context)
