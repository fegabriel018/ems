# Generated by Django 4.1.3 on 2024-04-20 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0016_remove_position_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='department_id',
        ),
        migrations.AddField(
            model_name='position',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='position',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
