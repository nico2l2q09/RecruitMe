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
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password1'])
		login(request, user)
		if request.user.is_authenticated():
			return HttpResponseRedirect('http://localhost:8000/profile')
	else:
		return render(request, 'index.html')
	


def signupPlayer(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CoachSignup(city=request.POST['city'],
		state=request.POST['state'],
		school=request.POST['school'],
		position=request.POST['position'],
		phone=request.POST['phone'],
		SAT=request.POST['SAT'],
		ACT=request.POST['ACT'],
		birthDate=request.POST['birthDate'])
		form1 = UserForm(username=request.POST['username'],
		first_name=request.POST['first_name'],
		last_name=request.POST['last_name'],
		email=request.POST['email'])
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
			new1 = form1.save()
			new = form.save(commit=False)
			new.username = new1
			new.save()
			
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/profile/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = CoachSignup()
		form1 = UserForm()
	return render(request, 'signupCoach.html', {'form': form, 'form1': form1})

def profile(request, username=None):
	if username:
		a_list = Coach.objects.filter(username=username)
		context = {'user_list': a_list}
		return render(request, 'coach.html', context)
	else: 
		if request.user.is_authenticated():
			a_list = Coach.objects.filter(username=request.user)
			context = {'user_list': a_list}
		return render(request, 'coach.html', context)

def playerProfile(request, username=None):
	if username:
		a_list = User.objects.filter(username=username)
		context = {'user_list': a_list}
		return render(request, 'player.html', context)
	else: 
		if request.user.is_authenticated():
			a_list = User.objects.filter(username=request.user)
			context = {'user_list': a_list}
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
