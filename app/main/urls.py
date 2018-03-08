#coding: utf-8

from django.conf.urls import url
from main.views import home, add_os, list_os, delete_os


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^nova_os/$', add_os, name='add_os'),
    url(r'^listar_os/$', list_os, name='list_os'),
    url(r'^apagar_os/(?P<pk>\d+)$', delete_os, name='delete_os'),
]
