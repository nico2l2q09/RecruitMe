# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Player(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	school = models.CharField(max_length=25)
	position = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phone = models.CharField(max_length=25)
	SAT = models.IntegerField()
	ACT = models.IntegerField()
	GPA = models.IntegerField()
	birthDate = models.DateField()



class Coach(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	school = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	phone = models.CharField(max_length=25)

