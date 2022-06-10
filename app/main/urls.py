#coding: utf-8

from django.urls import path
from main.views import home, add_os, list_os, delete_os


urlpatterns = [
    path('', home, name='home'),
    path('nova_os/', add_os, name='add_os'),
    path('listar_os/', list_os, name='list_os'),
    path('apagar_os/<pk>/', delete_os, name='delete_os'),
]
