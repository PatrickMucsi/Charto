# Generated by Django 3.0.8 on 2020-07-17 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20200717_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 17, 4, 17, 19, 765892), max_length=30),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='current_price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='referencecrypto',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 17, 4, 17, 19, 767408), max_length=30),
        ),
    ]
