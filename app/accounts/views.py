#coding: utf-8

from django.shortcuts import render


def create_account(request):
    template_name = 'accounts/register.html'
    context = {}
    return render(request, template_name, context)