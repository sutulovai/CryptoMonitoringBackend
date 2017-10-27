# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringBackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationuser',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicationuser',
            name='login',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]