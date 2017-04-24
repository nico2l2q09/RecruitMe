# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Player(models.Model):
	#first_name = models.CharField(max_length=25, default='Kayla')
	#last_name = models.CharField(max_length=25, default='Symanovich')
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	school = models.CharField(max_length=25)
	position = models.CharField(max_length=25)
	club = models.CharField(max_length=25, default='none')
	phone = models.CharField(max_length=25)
	SAT = models.IntegerField()
	ACT = models.IntegerField()
	GPA = models.IntegerField()
	birthDate = models.DateField()
	video = models.CharField(max_length=150, default='none')

	#video = models.CharField(max_length=150)


class Coach(models.Model):
	school = models.CharField(max_length=25)
	head_coach = models.CharField(max_length=50, default='none')
	assistant_coach = models.CharField(max_length=50, default='none')
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=25, default='none')
	league = models.CharField(max_length=25, default='none')

	#video = models.CharField(max_length=150)

	#logo = models.ImageField(upload_to = 'logos/', null=True)

