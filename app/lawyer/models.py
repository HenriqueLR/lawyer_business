#coding: utf-8

from django.db import models
from lawyer.utils import validate_cpf, validate_phone


class LawyerModel(models.Model):
    id_laywer = models.AutoField(primary_key=True, verbose_name=u'Cod Laywer', db_column='id_laywer')
    name = models.CharField(verbose_name='Nome', db_column='name', max_length=100)
    phone = models.CharField(verbose_name='Telefone', db_column='phone', max_length=14, validators=[validate_phone])
    email = models.EmailField(verbose_name=u'E-mail', unique=True, db_column='email')
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_cpf])
    updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')


    def __unicode__(self):
        return (u'%s - %s') % (self.cpf, self.name)

    class Meta:
        verbose_name = 'Advogado'
        verbose_name_plural = 'Advogados'
        ordering=['-created_at']
        db_table='lawyer'