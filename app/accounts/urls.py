#coding: utf-8

from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts.views import create_account

urlpatterns = [
    url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),
    url(r'^sair/$',logout,{'next_page':'accounts:login'},name='logout'),
    url(r'^registrar/$',create_account,name='create_account'),
]
