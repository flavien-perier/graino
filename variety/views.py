from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms

from django.http import HttpResponse
from django.shortcuts import render_to_response

from variety.models import Variety, Category

# Create your views here.
def index(request):
    v_variety = Variety.objects.all()
    return render_to_response('index.html', {'varieties': v_variety})

def VarietyListView(request):
    v_variety = Variety.objects.all()
    return render_to_response('variety_list.html', {'varieties': v_variety})

def CategoryListView(request):
    v_categories = Category.objects.all()
    return render_to_response('category_list.html', {'categories': v_categories})

def forms(request):
    return render_to_response('forms.html')

def reponse(request):

    v_nom = PostForm(request.POST)

    return render_to_response('reponse.html', {'nom': v_nom})
    
def recherche(request, category):
    v_variety = Variety.objects.filter(category__title=category)
    return render_to_response('variety_list.html', {'varieties': v_variety})