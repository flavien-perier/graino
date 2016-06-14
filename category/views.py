# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

from .forms import AddCategoryForm

# Category view


def category_list_view(request):
    v_categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': v_categories}, content_type='text/html')
    
def category_detail(request, categ):
    try:
        category = Category.objects.get(url=categ)
        if request.user.username:
            varieties_ids = Catalog.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
            inventory = Variety.objects.filter(pk__in=varieties_ids)
        else:
            inventory = 0
        nom_page = category.title

        descendant = category.get_descendants(include_self=False)
        ascendants = category.get_ancestors(ascending=False, include_self=False)
        
        categories = category.get_children()
        
        if not descendant:
            varieties = Variety.objects.filter(category__url=categ)
        else:
            varieties = Variety.objects.filter(category__in=descendant)
        
        return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'cat_parents':ascendants, 'nom_page':nom_page, 'inventory':inventory}, content_type='text/html')

    except:
        return render(request, '404.html', content_type='text/html')

def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddCategoryForm()
        
    return render(request, 'add_category.html', {'form' : form}, content_type='text/html')