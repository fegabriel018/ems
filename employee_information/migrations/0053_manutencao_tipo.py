# Generated by Django 4.1.3 on 2024-06-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0052_manutencao'),
    ]

    operations = [
        migrations.AddField(
            model_name='manutencao',
            name='tipo',
            field=models.CharField(default='', max_length=20),
        ),
    ]