# Generated by Django 4.1.3 on 2024-06-09 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0033_alter_contrato_valor_contratual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='tipo_contrato',
            field=models.CharField(blank=True, choices=[('venda', 'Venda'), ('aluguel', 'Aluguel')], max_length=100, null=True),
        ),
    ]
