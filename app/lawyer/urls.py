#coding: utf-8

from django.conf.urls import url
from lawyer.views import add_lawyer, list_os, sign_os, list_os_sign


urlpatterns = [
    url(r'^novo_advogado/$', add_lawyer, name='add_lawyer'),
    url(r'^listar_os/$', list_os, name='list_os'),
    url(r'^listar_os_assinada/$', list_os_sign, name='list_os_sign'),
    url(r'^assinar_os/(?P<pk>\d+)$', sign_os, name='sign_os'),
]
