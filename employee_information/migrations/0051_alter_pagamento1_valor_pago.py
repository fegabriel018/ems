# Generated by Django 4.1.3 on 2024-06-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0050_pagamento2_pagamento1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento1',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
