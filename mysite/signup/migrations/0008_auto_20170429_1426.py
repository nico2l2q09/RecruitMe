# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_remove_coach_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(default='media/1051px-Harvard_Wreath_Logo_1.svg.png', max_length=100000, upload_to='media/'),
        ),
    ]