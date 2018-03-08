#coding: utf-8

from django.contrib import admin
from main.models import StatusModel, OrderServiceModel, BusinessLawyerModel



class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)



class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ('business', 'title')



class BusinessLawyerAdmin(admin.ModelAdmin):
    list_display = ('order_service', 'price', 'lawyer', 'status')



admin.site.register(StatusModel, StatusAdmin)
admin.site.register(OrderServiceModel, OrderServiceAdmin)
admin.site.register(BusinessLawyerModel, BusinessLawyerAdmin)
