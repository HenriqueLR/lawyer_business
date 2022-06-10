#coding: utf-8

from django.urls import path
from business.views import add_business, list_os_validate, update_status_os


urlpatterns = [
    path('nova_empresa/', add_business, name='add_business'),
    path('listar_os_assindas/', list_os_validate, name='list_os_validate'),
    path('alterar_status_os/<key>/<pk>/', update_status_os, name='update_status_os'),
]
