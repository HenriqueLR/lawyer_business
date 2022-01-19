#coding: utf-8

from django.db import models
from business.models import BusinessModel
from lawyer.models import LawyerModel
from django.urls import reverse



class DefaultFieldsModel(models.Model):
    updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

    class Meta:
        abstract = True



class StatusModel(DefaultFieldsModel):
    id_status = models.AutoField(primary_key=True, verbose_name=u'Cod Status', db_column='id_status')
    name = models.CharField(verbose_name='Nome', db_column='name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering=['-created_at']
        db_table='status_order_service'



class OrderServiceManager(models.Manager):

    def filter_user(self, user):
        qs = super(OrderServiceManager, self).get_queryset()
        return qs.filter(business__user=user)



class OrderServiceModel(DefaultFieldsModel):
    id_order_service = models.AutoField(primary_key=True, verbose_name=u'Cod Order Service', db_column='id_order_service')
    business = models.ForeignKey(BusinessModel, verbose_name='Empresa',
                                related_name='order_service_business', db_column='business',
                                on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Titulo', db_column='title', max_length=50)
    description = models.TextField(db_column='description', verbose_name=u'Descricao')

    objects = OrderServiceManager()

    def __str__(self):
        return self.business.name

    def get_delete_os(self):
        return reverse('main:delete_os', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviços'
        ordering=['-created_at']
        db_table='order_business'



class BusinessLawyerManager(models.Manager):

    def filter_user(self, user):
        qs = super(BusinessLawyerManager, self).get_queryset()
        return qs.filter(order_service__business=user)

    def filter_lawyer(self, user):
        qs = super(BusinessLawyerManager, self).get_queryset()
        return qs.filter(lawyer=user)


class BusinessLawyerModel(DefaultFieldsModel):
    id_business_lawyer = models.AutoField(primary_key=True, verbose_name='Cod Business Lawyer',
                                            db_column='id_business_lawyer')
    order_service = models.ForeignKey(OrderServiceModel, verbose_name='Order Service',
                        related_name='business_lawyer_order_service', db_column='order_service',
                        on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Preço', db_column='price', null=False, blank=False,
                                max_digits=10, decimal_places=2)
    lawyer = models.ForeignKey(LawyerModel, verbose_name='Lawyer',
                        related_name='business_lawyer_lawyer', db_column='lawyer',
                        on_delete=models.CASCADE)
    status = models.ForeignKey(StatusModel, verbose_name='Status',
                                related_name='order_service_status', db_column='status',
                                on_delete=models.CASCADE)
    description = models.TextField(db_column='description', verbose_name=u'Descricao')

    objects = BusinessLawyerManager()

    def __str__(self):
        return (u'%s - %s') % (self.order_service, self.price)

    class Meta:
        verbose_name = 'Empresa Advogado'
        verbose_name_plural = 'Empresas Advogados'
        ordering=['-created_at']
        db_table='business_lawyer'
        unique_together = ('order_service', 'lawyer',)
