#coding: utf-8

from django.conf.urls import url
from business.views import add_business


urlpatterns = [
    url(r'^nova_empresa/$', add_business, name='add_business'),
]
