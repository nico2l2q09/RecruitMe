# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.template import loader
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	#template = loader.get_template('signup/index.html')

	#return HttpResponse(template.render(request))
	return render(request, 'signup/index.html')
# Create your views here.
