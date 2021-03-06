# Generated by Django 3.0.8 on 2020-07-17 03:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0006_auto_20200717_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencecrypto',
            name='current_time',
            field=models.CharField(default=datetime.datetime(2020, 7, 17, 3, 37, 30, 304457), max_length=30),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.CharField(max_length=100)),
                ('previous_balances', django_mysql.models.ListTextField(models.CharField(max_length=100), size=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
