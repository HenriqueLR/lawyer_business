#coding: utf-8

from django.conf.urls import url
from lawyer.views import add_lawyer


urlpatterns = [
    url(r'^novo_advogado/$', add_lawyer, name='add_lawyer'),
]
