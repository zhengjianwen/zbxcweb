# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbxc', '0005_aboutmodel_casemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZhaopinModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='职位名称')),
                ('xueli', models.SmallIntegerField(choices=[(1, '博士'), (2, '研究生'), (3, '本科'), (4, '专科')], default=3, verbose_name='学历')),
                ('age_s', models.CharField(default='18-35', max_length=64, verbose_name='年龄段')),
                ('qualifications', models.TextField(verbose_name='职位描述')),
                ('requirement', models.TextField(verbose_name='任职要求')),
                ('weight', models.SmallIntegerField(default=1, verbose_name='权重')),
                ('status', models.BooleanField(default=0, verbose_name='显示/关闭')),
                ('ctime', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '客户案例',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutmodel',
            options={'verbose_name_plural': '关于我们'},
        ),
    ]
