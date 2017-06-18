# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render #, HttpResponse

# Create your views here.
def index(request):
    print '*'*50
    return render(request, 'realportfolioapp/index.html')

def about(request):
    print '$'*50
    return render(request, 'realportfolioapp/about.html')

def projects(request):
    print '^'*50
    return render(request, 'realportfolioapp/projects.html')

def testimonials(request):
    print '&'*50
    return render(request, 'realportfolioapp/testimonials.html')