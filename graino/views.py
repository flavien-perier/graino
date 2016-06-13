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
    categ = Category.objects
    
    return render(request, 'accueil.html', {
        'aromatiques': categ.get(url='aromatiques'),
        'legumes_feuilles': categ.get(url='legumes-feuilles'),
        'fruitiers': categ.get(url='fruitiers'),
        'legumes_racines': categ.get(url='legumes-racines'),
        'medicinales': categ.get(url='medicinales'),
        'graines_potageres': categ.get(url='graines-potageres')
    }, content_type='text/html')

def aide(request):
    return render(request, 'help.html', content_type='text/html')
