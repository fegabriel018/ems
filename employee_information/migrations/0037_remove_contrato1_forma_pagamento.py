# Generated by Django 4.1.3 on 2024-06-11 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0036_remove_contrato_tipo_contrato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato1',
            name='forma_pagamento',
        ),
    ]
