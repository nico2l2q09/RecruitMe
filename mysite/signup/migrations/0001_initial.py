# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 18:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=25)),
                ('head_coach', models.CharField(default='none', max_length=50)),
                ('assistant_coach', models.CharField(default='none', max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(default='none', max_length=25)),
                ('league', models.CharField(default='none', max_length=25)),
                ('video', models.CharField(default='none', max_length=150)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('coach_id', models.IntegerField()),
                ('p_interest', models.IntegerField(default=5)),
                ('c_interest', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('school', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=25)),
                ('club', models.CharField(default='none', max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('SAT', models.IntegerField()),
                ('ACT', models.IntegerField()),
                ('GPA', models.DecimalField(decimal_places=2, max_digits=3)),
                ('birthDate', models.DateField()),
                ('video', models.CharField(default='none', max_length=150)),
                ('grad_year', models.CharField(default='none', max_length=10)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
