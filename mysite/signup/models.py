# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
	#first_name = models.CharField(max_length=25, default='Kayla')
	#last_name = models.CharField(max_length=25, default='Symanovich')
	username = models.OneToOneField(User)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	school = models.CharField(max_length=75)
	position = models.CharField(max_length=25)
	club = models.CharField(max_length=25, default='none')
	phone = models.CharField(max_length=25)
	SAT = models.IntegerField()
	ACT = models.IntegerField()
	GPA = models.DecimalField(decimal_places=2, max_digits=3)
	birthDate = models.DateField()
	video = models.CharField(max_length=150, default='none')
	grad_year = models.CharField(max_length=10, default='none')


	#video = models.CharField(max_length=150)


class Coach(models.Model):
	username = models.OneToOneField(User)
	school = models.CharField(max_length=25)
	head_coach = models.CharField(max_length=50, default='none')
	assistant_coach = models.CharField(max_length=50, default='none')
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=25, default='none')
	league = models.CharField(max_length=25, default='none')
	video = models.CharField(max_length=150, default='none')
	#video = models.CharField(max_length=150)

	#logo = models.ImageField(upload_to = 'logos/', null=True)

class Matches(models.Model):
	player_id = models.IntegerField()
	coach_id = models.IntegerField()
	p_interest = models.IntegerField(default=5)
	c_interest = models.IntegerField(default=5)



