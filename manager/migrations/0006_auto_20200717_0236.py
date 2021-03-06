# Generated by Django 3.0.8 on 2020-07-17 02:36

import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_referencecrypto_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencecrypto',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 17, 2, 36, 50, 767340), max_length=30),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='previous_prices_times',
            field=django_mysql.models.ListTextField(models.CharField(max_length=30), size=None),
        ),
    ]
