# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lawyer', '0001_initial'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessLawyerModel',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Atualizado em')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Criado em')),
                ('id_business_lawyer', models.AutoField(db_column='id_business_lawyer', primary_key=True, serialize=False, verbose_name='Cod Business Lawyer')),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('description', models.TextField(db_column='description', verbose_name='Descricao')),
                ('lawyer', models.ForeignKey(db_column='lawyer', on_delete=django.db.models.deletion.CASCADE, related_name='business_lawyer_lawyer', to='lawyer.LawyerModel', verbose_name='Lawyer')),
            ],
            options={
                'verbose_name': 'Empresa Advogado',
                'verbose_name_plural': 'Empresas Advogados',
                'db_table': 'business_lawyer',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderServiceModel',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Atualizado em')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Criado em')),
                ('id_order_service', models.AutoField(db_column='id_order_service', primary_key=True, serialize=False, verbose_name='Cod Order Service')),
                ('title', models.CharField(db_column='title', max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(db_column='description', verbose_name='Descricao')),
                ('business', models.ForeignKey(db_column='business', on_delete=django.db.models.deletion.CASCADE, related_name='order_service_business', to='business.BusinessModel', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Ordem de Serviço',
                'verbose_name_plural': 'Ordens de Serviços',
                'db_table': 'order_business',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='StatusModel',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Atualizado em')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Criado em')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Descricao')),
                ('id_status', models.AutoField(db_column='id_status', primary_key=True, serialize=False, verbose_name='Cod Status')),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'db_table': 'status_order_service',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='businesslawyermodel',
            name='order_service',
            field=models.ForeignKey(db_column='order_service', on_delete=django.db.models.deletion.CASCADE, related_name='business_lawyer_order_service', to='main.OrderServiceModel', verbose_name='Order Service'),
        ),
        migrations.AddField(
            model_name='businesslawyermodel',
            name='status',
            field=models.ForeignKey(db_column='status', on_delete=django.db.models.deletion.CASCADE, related_name='order_service_status', to='main.StatusModel', verbose_name='Status'),
        ),
        migrations.AlterUniqueTogether(
            name='businesslawyermodel',
            unique_together=set([('order_service', 'lawyer')]),
        ),
    ]
