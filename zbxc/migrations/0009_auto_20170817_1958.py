# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-17 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbxc', '0008_auto_20170606_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filiale',
            name='img',
            field=models.CharField(max_length=255, verbose_name='图片'),
        ),
    ]
