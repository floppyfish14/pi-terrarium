# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempsensor', '0010_auto_20170228_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='Temp_F',
            field=models.IntegerField(),
        ),
    ]