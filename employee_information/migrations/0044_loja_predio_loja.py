# Generated by Django 4.1.3 on 2024-06-11 23:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0043_delete_loja1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('status', models.IntegerField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('predio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lojas', to='employee_information.predio')),
            ],
        ),
        migrations.AddField(
            model_name='predio',
            name='loja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predios', to='employee_information.loja'),
        ),
    ]
