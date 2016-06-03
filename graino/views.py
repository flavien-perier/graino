from django.shortcuts import render, HttpResponse 
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

# Graino view


def index(request):
    return render_to_response('index.html')

def aide(request):
    return render_to_response('help.html')