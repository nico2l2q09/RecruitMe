# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CoachSignup
from .forms import PlayerSignup
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
		print "ok"
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			new = form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/playerProfile')
	else: 
		form = PlayerSignup()
	return render(request, 'signupPlayer.html', {'form': form})

def getSignuphtml():
	f =  open("signup/signupPlayer.html", "r")
	r = f.read()
	return r

def signupCoach(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = CoachSignup(request.POST)
		print "ok"
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			new = form.save()
			# redirect to a new URL:
			return HttpResponseRedirect('http://localhost:8000/profile/')

	# if a GET (or any other method) we'll create a blank form
	else: 
		form = CoachSignup()
	return render(request, 'signupCoach.html', {'form': form})

def profile(request):
	a = """<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
  <title>Bootstrap Theme Simply Me</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  .img-circle {
    border:3px solid #555555;
  }
  .bg-1 { 
      background-color: #ffffff;
      color: #555555;
  }
  .bg-2 { 
      background-color: #474e5d;
      color: #ffffff;
  }
  .container-fluid {
      padding-top: 30px;
      padding-bottom: 30px;
  }
  </style>
<link rel = "stylesheet"
   type = "text/css"
   href = "myStyle.css" />
</head>
<body>
<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span> 
      </button>
      <a class="navbar-brand" href="#">Me</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">WHO</a></li>
        <li><a href="#">WHAT</a></li>
        <li><a href="#">WHERE</a></li>
      </ul>
    </div>
  </div>
</nav>
<div class="container-fluid bg-1 text-center">
  <h3>  Princeton </h3>
  <img src="https://studyqa.com/media/upload/univers/840/51/princeton-university-uni_profile_84051.jpg" class="img-circle" alt="Goodies" width="350" height="350">
  <h4>Class of 2018 at  San Francisco University High School</h4> 
  <h4>Forward for Marin FC</h4>
  <h4>I'm looking to get recruited by a great school</h4>
</div>

<div class="container-fluid bg-2 text-center">
  <h3>Information</h3>
<center>"""
	print (Coach.objects.values('school'), Coach.objects.values('first_name'))

	b = """<p><font face="verdana" color="white"><strong>League:</strong> %s </font></p>
	<p><font face="verdana" color="white"><strong>Head Coach:</strong> %s </font></p>
	<p><font face="verdana" color="white"><strong>Assistant Coach:</strong> %s </font></p>
	<p><font face="verdana" color="white"><strong>School Website:</strong> %s </font></p>
	<p><font face="verdana" color="white"><strong>Program Website:</strong> %s </font></p>""" % (Coach.objects.values('first_name'), Coach.objects.values('school'),Coach.objects.values('first_name'),Coach.objects.values('first_name'),Coach.objects.values('first_name'))
	return HttpResponse(a)

def playerProfile(request):
	f = open("signup/player.html", "r")
	r = f.read()
	return HttpResponse(r)
#def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	#return render(request, 'signup/index.html')
# Create your views here.
