#coding: utf-8

from django.conf.urls import url
from business.views import add_business, list_os_validate, update_status_os


urlpatterns = [
    url(r'^nova_empresa/$', add_business, name='add_business'),
    url(r'^listar_os_assindas/$', list_os_validate, name='list_os_validate'),
    url(r'^alterar_status_os/(?P<key>[\w\-]+)/(?P<pk>\d+)$', update_status_os, name='update_status_os'),
]
