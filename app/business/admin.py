#coding: utf-8

from django.contrib import admin
from business.models import BusinessModel



class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)



admin.site.register(BusinessModel, BusinessAdmin)
