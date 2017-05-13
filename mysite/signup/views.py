# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CoachSignup
from .forms import PlayerSignup
from .forms import position
from .forms import UserForm
from .forms import UpdatePlayerProfile
from .forms import UpdateCoachProfile
from django.contrib.auth.models import User
from signup.models import Coach, Player, Matches
from django.views.generic.edit import UpdateView


def index(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		login(request, user)
		if user and user.is_authenticated:
			if Coach.objects.filter(username=request.user):
				a_list = Coach.objects.filter(username=request.user)
				context = {'user_list': a_list}
				return render(request, 'coach_nobuttons.html', context)
			else: 
				a_list = Player.objects.filter(username=request.user)
				context = {'player_list': a_list}
				return render(request, 'player_nobuttons.html', context)
	return render(request, 'index.html')

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'city', 'state', 'school', 'position', 'club', 'phone', 'SAT', 'ACT', 'GPA', 'birthDate', 'video', 'grad_year', 'photo']
    template_name_suffix = '_update_form'


def updateProfile(request):
	if request.method == 'POST':
		if Player.objects.filter(username=request.user):
			print "2"
			player = Player.objects.get(username=request.user)
			form = UpdatePlayerProfile(request.POST, request.FILES, instance=player)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/profile/')
		else:
			coach = Coach.objects.get(username=request.user)
			form = UpdateCoachProfile(request.POST, request.FILES, instance=coach)
			print coach.photo.url
			if form.is_valid():
				form.save()
			return HttpResponseRedirect('/profile/')
		
	else:
		if Player.objects.filter(username=request.user):
			print "x"
			player = Player.objects.get(username=request.user)
			form = UpdatePlayerProfile(initial={'name':player.name}, instance=player)
		else:
			coach = Coach.objects.get(username=request.user)
			form = UpdateCoachProfile(initial={'name':coach.head_coach}, instance=coach)
	return render(request, 'update_profile.html', {'form': form})


	# if request.method == 'POST':
	# 	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	# 	login(request, user)
	# 	print "success"
	# 	if request.user.is_authenticated():
	# 		if Coach.objects.filter(username=request.user):
	# 			a_list = Coach.objects.filter(username=request.user)
	# 			context = {'user_list': a_list}
	# 			return render(request, 'coach.html', context)
	# 		else: 
	# 			a_list = Player.objects.filter(username=request.user)
	# 			context = {'player_list': a_list}
	# 			return render(request, 'player.html', context)
	# else:
	# 	print "else"
	# 	return render(request, 'index.html')
	
def logoutuser(request):
	logout(request)
	return render(request, 'index.html')

def signupPlayer(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		
		form = PlayerSignup(request.POST, request.FILES)
		form1 = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid() and form1.is_valid():
			# process the data in form.cleaned_data as required
			new1 = form1.save()
			new = form.save(commit=False)
			#new.name = request.POST["first_name"] + " " + request.POST["last_name"]
			new.username = new1
			new.save()
			
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			# redirect to a new URL:
			return HttpResponseRedirect('/profile/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = PlayerSignup()
		form1 = UserForm()
	return render(request, 'signupPlayer.html', {'form': form, 'form1': form1})

def signupCoach(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		print("signing up...")
		form = CoachSignup(request.POST, request.FILES)
		form1 = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid() and form1.is_valid():
			# process the data in form.cleaned_data as required
			new1 = form1.save()
			new = form.save(commit=False)
			new.username = new1

			new.save()
			"saved"
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)
			# redirect to a new URL:
			return HttpResponseRedirect('/profile/')
		# if a GET (or any other method) we'll create a blank form
	else: 
		form = CoachSignup()
		form1 = UserForm()
	return render(request, 'signupCoach.html', {'form': form, 'form1': form1})

# def profile(request, username=None):
	
# 	if username:
# 		a_list = Coach.objects.filter(username=username)
# 		context = {'user_list': a_list}
# 		return render(request, 'coach.html', context)
# 	else: 
# 		if request.user.is_authenticated():
# 			a_list = Coach.objects.filter(username=request.user)
# 			context = {'user_list': a_list}
# 		return render(request, 'coach.html', context)

def profile(request, username=None):
	print request.user
	if username is not None:
		if Coach.objects.filter(username=username):
			if Coach.objects.get(username=username).username == request.user:
				print "coach logged on"
				a_list = Coach.objects.filter(username=request.user)
				context = {'user_list': a_list}
				return render(request, 'coach_nobuttons.html', context)
			elif Coach.objects.filter(username=username):
				print "coach reg"
				a_list = Coach.objects.filter(username=username)
				context = {'user_list': a_list}
				return render(request, 'coach.html', context)
		elif Player.objects.filter(username=username):
			if Player.objects.get(username=username).username == request.user:
				print "player logged on"
				a_list = Player.objects.filter(username=request.user)
				context = {'player_list': a_list}
				return render(request, 'player_nobuttons.html', context)
			elif Player.objects.filter(username=username):
				print "player reg"
				a_list = Player.objects.filter(username=username)
				context = {'player_list': a_list}
				return render(request, 'player.html', context)
	else:
		if Coach.objects.filter(username=request.user):
				print "coach logged on"
				a_list = Coach.objects.filter(username=request.user)
				context = {'user_list': a_list}
				return render(request, 'coach_nobuttons.html', context)
		elif Player.objects.filter(username=request.user):
				print "player logged ON"
				a_list = Player.objects.filter(username=request.user)
				context = {'player_list': a_list}
				return render(request, 'player_nobuttons.html', context)
	
	# if username is not None:
	# 	if Player.objects.filter(username=request.user):
	# 		a_list = Player.objects.filter(username=request.user)
	# 		context = {'player_list': a_list}
	# 		return render(request, 'player_nobuttons.html', context)
		

	# 	elif Coach.objects.filter(username=request.user):
	# 		print "myprofile player"
	# 		a_list = Coach.objects.filter(username=request.user)
	# 		context = {'user_list': a_list}
	# 		return render(request, 'coach.html', context)
		
	# else: 
	# 	#if request.user.is_authenticated():

	# 	print "xx"
		
def explore(request):
	if request.user.is_authenticated():
		if Coach.objects.filter(username=request.user):
			if request.method == 'POST':
				if request.POST["position"] == 'All':
					a_list = Player.objects.all()
				else:
					a_list = Player.objects.filter(position=request.POST["position"])

				if request.POST["gpa"]:
					var = request.POST["gpa"]
					print var
					a_list = a_list.filter(GPA__gt=var)

				form = position(request.POST)
				context = {'user_list': a_list, 'form': form}
				return render(request, 'explorePlayer.html', context)
			else:
				a_list = Player.objects.all()
				form = position()
				context = {'user_list': a_list, 'form': form}
				return render(request, 'explorePlayer.html', context)
		else: 
			a_list = Coach.objects.all()
			context = {'user_list': a_list}
			return render(request, 'exploreCoach.html', context)



	# if request.user.is_authenticated():
	# 	if Coach.objects.filter(username=request.user):
	# 		a_list = Player.objects.all()
	# 		form = position()
	# 		context = {'user_list': a_list, 'form': form}
	# 		return render(request, 'explorePlayer.html', context)
	# 	else: 
	# 		a_list = Coach.objects.all()
	# 		context = {'user_list': a_list}
	# 		return render(request, 'exploreCoach.html', context)


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
			print "coach is logged on"
			a1_list = []
			a_list = Matches.objects.filter(interested=request.user)
			for ID in a_list:
				obj = matches.objects.filter(interestee=request.user).filter(interested=ID.interestee)
				if obj:
					a1_list.append(Player.objects.get(obj.interested))
				print a1_list
		else:
			print "player is logged on"
			a1_list = []
			a_list = Matches.objects.filter(interested=request.user)
			for ID in a_list:
				obj = matches.objects.filter(interestee=request.user).filter(interested=ID.interestee)
				if obj:
					a1_list.append(Coach.objects.get(obj.interested))
				print a1_list
		context = {'matches_list': a1_list}
		return render(request, 'matchesPlayer.html', context)

def makeMatch(request, username):
	if matches.objects.filter(interestee=username).filter(interested=request.user):
		return 
	else: 
		match = matches(interested=request.user, interestee=username)
		match.save()
		return 


def noInterest(request):
	return None

def matches(request):
	if request.user.is_authenticated():
		if Coach.objects.filter(username=request.user):
			a1_list = []
			a_list = Matches.objects.filter(interested=request.user)
			for ID in a_list:
				try:
					obj = Matches.objects.get(interestee=request.user, interested=ID.interestee)
				except:
					obj = None
				if obj:
					a1_list.append(Player.objects.get(username=obj.interested))
				print a1_list
			context = {'matches_list': a1_list}
			return render(request, 'matchesCoach.html', context)
		else:
			a1_list = []
			a_list = Matches.objects.filter(interested=request.user)
			for ID in a_list:
				print ID
				try:
					obj = Matches.objects.get(interestee=request.user, interested=ID.interestee)
				except:
					obj = None
				if obj:
					a1_list.append(Coach.objects.get(username=obj.interested))
				print a1_list
			context = {'matches_list': a1_list}
			return render(request, 'matchesPlayer.html', context)

def makeMatch(request, username):
	if Matches.objects.filter(interestee=username).filter(interested=request.user):
		return HttpResponseRedirect('/profile/' + username)
	else: 
		match = Matches()
		match.interested =request.user
		match.interestee = User.objects.get(id=username)
		match.save()
		return HttpResponseRedirect('/profile/' + username)
