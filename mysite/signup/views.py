# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	html = gethtml()
	return HttpResponse(html)

def gethtml():
	f =  open("signup/index.html", "r")
	r = f.read()
	return r

def signup(request):
	html = getSignuphtml()
	return HttpResponse(html)

def getSignuphtml():
	f =  open("signup/signup.html", "r")
	r = f.read()
	return r

def signupCoach(request):
	f = open("signup/signupCoach.html", "r")
	r = f.read()
	return HttpResponse(r)

def profile(request):
	f = open("signup/coach.html", "r")
	r = f.read()
	return HttpResponse(r)

def playerProfile(request):
	f = open("signup/player.html", "r")
	r = f.read()
	return HttpResponse(r)
#def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	#return render(request, 'signup/index.html')
# Create your views here.
