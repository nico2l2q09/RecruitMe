# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20170428_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='photo',
            field=models.ImageField(max_length=100000, upload_to='/Users/kaykaybug/Desktop/RecruitMe/recruitme/mysite/signup/media'),
        ),
    ]
