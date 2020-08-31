# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 02:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tempsensor', '0004_remove_temperature_temp_f'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='Temp_F',
            field=models.CharField(default=datetime.datetime(2017, 2, 26, 2, 54, 26, 849737, tzinfo=utc), max_length=3),
            preserve_default=False,
        ),
    ]