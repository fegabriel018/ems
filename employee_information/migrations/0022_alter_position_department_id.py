# Generated by Django 4.1.3 on 2024-04-20 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0021_position_department_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='department_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_information.department'),
        ),
    ]
