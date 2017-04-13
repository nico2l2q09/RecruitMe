from django.shortcuts import render
from django.http import HttpResponse

def coach(request):
	f = open("profile/coach.html", "r")
	r = f.read()
	return HttpResponse(r)

def player(request):
	f = open("profile/player.html", "r")
	r = f.read()
	return HttpResponse(r)
# Create your views here.
