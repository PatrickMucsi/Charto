# Generated by Django 3.0.8 on 2020-07-17 02:11

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20200717_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencecrypto',
            name='previous_prices_times',
            field=django_mysql.models.ListTextField(models.CharField(max_length=15), default='pussy', size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='previous_prices',
            field=django_mysql.models.ListTextField(models.CharField(max_length=15), size=None),
        ),
    ]
