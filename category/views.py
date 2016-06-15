# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
from django.db.models import Q
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

from .forms import AddCategoryForm

# Category view


def category_list_view(request):
    if request.method == "POST" and request.POST["search"]:
        tree = 0
        search = request.POST["search"].split(" ")
        
        req_categ = Q(title__contains=request.POST["search"])
        req_variet = Q(title__contains=request.POST["search"])
        for o in search:
            tmp_categ = Q(title__contains=o) | Q(url__contains=o)
            req_categ = req_categ | tmp_categ
            
            tmp_variet = Q(title__contains=o) | Q(latin__contains=o) | Q(url__contains=o)
            req_variet = req_variet | tmp_variet
        
        categories = Category.objects.filter(req_categ)
        varieties = Variety.objects.filter(req_variet)
        
    else:
        tree = 1
        categories = Category.objects.all()
        varieties = ""
        
    return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'tree':tree}, content_type='text/html')
    
def category_detail(request, categ):
    try:
        category = Category.objects.get(url=categ)
        if request.user.username:
            varieties_ids = Catalog.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
            inventory = Variety.objects.filter(pk__in=varieties_ids)
        else:
            inventory = 0
        nom_page = category.title
        url_page = category.url

        descendant = category.get_descendants(include_self=False)
        ascendants = category.get_ancestors(ascending=False, include_self=False)
        
        categories = category.get_children()
        
        if not descendant:
            varieties = Variety.objects.filter(category__url=categ)
        else:
            varieties = Variety.objects.filter(category__in=descendant)
        
        return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'cat_parents':ascendants, 'nom_page':nom_page, 'url_page':url_page, 'inventory':inventory, 'tree':1}, content_type='text/html')

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