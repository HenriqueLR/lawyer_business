#coding: utf-8

from lawyer.models import LawyerModel
from business.models import BusinessModel
from django.contrib import messages
from django.shortcuts import redirect


def user_check(view):
    def wrap(request, *args, **kwargs):
        business = BusinessModel.objects.filter(user=request.user)
        lawyer = LawyerModel.objects.filter(user=request.user)

        if business.exists():
            return redirect('main:list_os')
        elif lawyer.exists():
            return redirect('lawyer:list_os')

        return view(request, *args, **kwargs)
    wrap.__doc__ = view.__doc__
    wrap.__name__ = view.__name__
    return wrap