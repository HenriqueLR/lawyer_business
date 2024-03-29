
from django.db import models
from django.contrib.auth.models import User


class BusinessModel(models.Model):
    id_business = models.AutoField(primary_key=True, verbose_name=u'Cod Business', db_column='id_business')
    name = models.CharField(verbose_name='Nome', db_column='name', max_length=100)
    updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')
    user = models.OneToOneField(User, verbose_name='Usuario', related_name='business_user', db_column='user', 
                                unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering=['-created_at']
        db_table='business'