"""hellow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_setup/', TemplateView.as_view(template_name="tests/setup.html",
                                            content_type="text/html"), name="test_setup"),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('advogados/', include(('lawyer.urls', 'lawyer'), namespace='lawyer')),
    path('empresas/', include(('business.urls', 'business'), namespace='business')),
    path('contas/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]


urlpatterns += staticfiles_urlpatterns()
