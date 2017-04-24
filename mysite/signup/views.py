# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CoachSignup
from .forms import PlayerSignup
from .forms import UserForm
from django.contrib.auth.models import User
from signup.models import Coach, Player

def index(request):
	html = gethtml()
	return HttpResponse(html)

def gethtml():
	f =  open("signup/index.html", "r")
	r = f.read()
	return r

def signupPlayer(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CoachSignup(request.POST)
		form1 = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid() and form1.is_valid():
			# process the data in form.cleaned_data as required
			new = form.save()
			new1 = form1.save()
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/playerProfile')
	else: 
		form = PlayerSignup()
		form1 = UserForm()
	return render(request, 'signupPlayer.html', {'form': form, 'form1': form1})

def getSignuphtml():
	f =  open("signup/signupPlayer.html", "r")
	r = f.read()
	return r

def signupCoach(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CoachSignup(request.POST)
		form1 = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid() and form1.is_valid():
			# process the data in form.cleaned_data as required
			new = form.save()
			new1 = form1.save()
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/profile/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = CoachSignup()
		form1 = UserForm()
	return render(request, 'signupCoach.html', {'form': form, 'form1': form1})

def profile(request):
	a_list = Coach.objects.filter(first_name='Nico')
	context = {'name': 'Nico', 'user_list': a_list}
	return render(request, 'coach.html', context)

def playerProfile(request):
	a_list = Player.objects.filter(first_name='Nico')
	context = {'name': 'Nico', 'player_list': a_list}
	return render(request, 'player.html', context)

def exploreCoach(request):
	a_list = Coach.objects.all()
	context = {'name': 'Mikaela', 'user_list': a_list}
	return render(request, 'exploreCoach.html', context)

def explorePlayer(request):
	a_list = Player.objects.all()
	context = {'player_list': a_list}
	return render(request, 'explorePlayer.html', context)
#def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	#return render(request, 'signup/index.html')
# Create your views here.
