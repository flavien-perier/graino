from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

from django.http import HttpResponse
from django.shortcuts import render_to_response

from variety.models import Variety, Category

# Create your views here.

def variety_list_view(request):
    v_variety = Variety.objects.all()
    return render_to_response('variety_list.html', {'varieties': v_variety})

def category_list_view(request):
    v_categories = Category.objects.all()
    return render_to_response('category_list.html', {'categories': v_categories})

def category_detail(request, category):
    v_variety = Variety.objects.filter(category__url=category)
    return render_to_response('variety_list.html', {'varieties': v_variety})

def forms(request):
    return render_to_response('forms.html')

def reponse(request):
    v_nom = PostForm(request.POST)
    return render_to_response('reponse.html', {'nom': v_nom})

def update(request):
    for o in Category.objects.all():
        o.url = slugify(o.title)
        o.save()