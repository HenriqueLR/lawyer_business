#coding: utf-8

from django.urls import path, reverse_lazy
from accounts.views import create_account
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('sair/',LogoutView.as_view(next_page=reverse_lazy('accounts:login')),name='logout'),
    path('registrar/',create_account,name='create_account'),
]
