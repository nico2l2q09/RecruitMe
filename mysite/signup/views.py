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
from signup.models import Coach, Player, Matches

def index(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		login(request, user)
		print "success"
		if request.user.is_authenticated():
			if Coach.objects.filter(username=request.user):
				a_list = Coach.objects.filter(username=request.user)
				context = {'user_list': a_list}
				return render(request, 'coach.html', context)
			else: 
				a_list = Player.objects.filter(username=request.user)
				context = {'player_list': a_list}
				return render(request, 'player.html', context)
	else:
		print "else"
		return render(request, 'index.html')
	


def signupPlayer(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		
		form = PlayerSignup(request.POST)
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
			return HttpResponseRedirect('http://localhost:8000/playerProfile/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = PlayerSignup()
		form1 = UserForm()
	return render(request, 'signupPlayer.html', {'form': form, 'form1': form1})

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
	print username
	if username:
		a_list = Player.objects.filter(username=username)
		context = {'player_list': a_list}
		return render(request, 'player.html', context)
	else: 
		if request.user.is_authenticated():
			a_list = Player.objects.filter(username=request.user)
			context = {'player_list': a_list}
		return render(request, 'player.html', context)

def explore(request):
	if request.user.is_authenticated():
		if Coach.objects.filter(username=request.user):
			a_list = Player.objects.all()
			context = {'user_list': a_list}
			return render(request, 'explorePlayer.html', context)
		else: 
			a_list = Coach.objects.all()
			context = {'user_list': a_list}
			return render(request, 'exploreCoach.html', context)


	# a_list = Coach.objects.all()
	# context = {'user_list': a_list}
	# return render(request, 'exploreCoach.html', context)

	# a_list = Player.objects.all()
	# context = {'player_list': a_list}
	# return render(request, 'explorePlayer.html', context)

# def explorePlayer(request):
# 	a_list = Player.objects.all()
# 	context = {'player_list': a_list}
# 	return render(request, 'explorePlayer.html', context)

def matches(request):
	if request.user.is_authenticated():
		if Coach.objects.filter(username=request.user):
			a1_list = []
			a_list = Matches.objects.filter(p_interest=1, c_interest=1).values_list('player_id')
			for ID in a_list:
				print ID[0] # gives player id where both fields are 1
				obj = Player.objects.filter(id=ID[0])
				#obj = Player.objects.get(username_id=ID[0])
				print obj[0]
				a1_list.append(obj[0])

			context = {'matches_list': a1_list}
			return render(request, 'matchesCoach.html', context)
		else:
			a1_list = []
			a_list = Matches.objects.filter(p_interest=1, c_interest=1).values_list('coach_id')
			for ID in a_list:
				obj = Coach.objects.filter(id=ID[0])
				a1_list.append(obj[0])
				print a1_list

			context = {'matches_list': a1_list}
			return render(request, 'matchesPlayer.html', context)

# def matchesCoach(request):
# 	a1_list = []
# 	a_list = Matches.objects.filter(p_interest=1, c_interest=1).values_list('player_id')
# 	for ID in a_list:
# 		print ID[0] # gives player id where both fields are 1
# 		obj = Player.objects.filter(id=ID[0])
# 		#obj = Player.objects.get(username_id=ID[0])
# 		print obj[0]
# 		a1_list.append(obj[0])

# 	context = {'matches_list': a1_list}
# 	return render(request, 'matchesCoach.html', context)

#def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	#return render(request, 'signup/index.html')
# Create your views here.
