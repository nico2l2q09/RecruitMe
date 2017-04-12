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

#def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	#return render(request, 'signup/index.html')
# Create your views here.
