# Generated by Django 3.0.8 on 2020-07-20 19:39

import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20200717_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 20, 19, 39, 52, 829153), max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='previous_balances_times',
            field=django_mysql.models.ListTextField(models.CharField(default=datetime.datetime(2020, 7, 20, 19, 39, 52, 829319), max_length=30), size=None),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 20, 19, 39, 52, 830724), max_length=30),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='previous_prices',
            field=django_mysql.models.ListTextField(models.CharField(default='0', max_length=15), size=None),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='previous_prices_times',
            field=django_mysql.models.ListTextField(models.CharField(default=datetime.datetime(2020, 7, 20, 19, 39, 52, 830896), max_length=30), size=None),
        ),
    ]
