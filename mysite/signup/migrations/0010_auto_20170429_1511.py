# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(default='media/athletics-logo.jpg', max_length=100000, upload_to='media/'),
        ),
    ]