#coding: utf-8

from django.contrib import admin
from lawyer.models import LawyerModel



class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'cpf')
    search_fields = ('name','cpf')



admin.site.register(LawyerModel, LawyerAdmin)
