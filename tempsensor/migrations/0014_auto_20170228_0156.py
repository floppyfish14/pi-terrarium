# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsensor', '0013_auto_20170228_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='Humidity_Percent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='reading_time',
            field=models.DateTimeField(verbose_name='date output'),
        ),
    ]
