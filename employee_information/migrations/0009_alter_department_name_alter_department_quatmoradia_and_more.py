# Generated by Django 4.1.3 on 2024-04-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0008_rename_status_employees_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='quatMoradia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='quatQ',
            field=models.IntegerField(),
        ),
    ]