# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Player(models.Model):
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	school = models.CharField(max_length=25)
	position = models.CharField(max_length=25)
	phone = models.CharField(max_length=25)
	SAT = models.IntegerField()
	ACT = models.IntegerField()
	GPA = models.IntegerField()
	birthDate = models.DateField()
	#video = models.CharField(max_length=150)


class Coach(models.Model):
	school = models.CharField(max_length=25)
	phone = models.CharField(max_length=25)
	video = models.CharField(max_length=150)

	#logo = models.ImageField(upload_to = 'logos/', null=True)

