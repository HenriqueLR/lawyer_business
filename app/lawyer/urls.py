#coding: utf-8

from django.urls import path
from lawyer.views import add_lawyer, list_os, sign_os, list_os_sign


urlpatterns = [
    path('novo_advogado/', add_lawyer, name='add_lawyer'),
    path('listar_os/', list_os, name='list_os'),
    path('listar_os_assinada/', list_os_sign, name='list_os_sign'),
    path('assinar_os/<pk>/', sign_os, name='sign_os'),
]
