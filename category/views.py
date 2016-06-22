# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
from django.db.models import Q
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from dal import autocomplete

from variety.models import *

from .forms import AddCategoryForm, SearchForm

import unicodedata

# Category view


def category_list_view(request):
    categories = Category.objects.all()
    varieties = ""
    form_search = SearchForm
    return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'tree':1, 'form_search':form_search}, content_type='text/html')
    
def search(request):
    if request.method == "GET" and request.GET["search"]:
        if request.user.username:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group=="user":
                varieties_ids = Catalog.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
                inventory = Variety.objects.filter(pk__in=varieties_ids)
                varieties_ids = Desire.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
                demande = Variety.objects.filter(pk__in=varieties_ids)
            else:
                varieties_ids = Catalog_group.objects.filter(group=Group.objects.get(pk=group)).values_list('variety', flat=True)
                inventory = Variety.objects.filter(pk__in=varieties_ids)
                varieties_ids = Desire_group.objects.filter(group=Group.objects.get(pk=group)).values_list('variety', flat=True)
                demande = Variety.objects.filter(pk__in=varieties_ids)
        else:
            inventory = 0
            demande = 0
    
        recherche = request.GET["search"]
        recherche =  unicodedata.normalize('NFD', recherche).encode('ascii', 'ignore')     
        search = recherche.split(" ")
        
        req_categ = Q(title__contains=recherche)
        req_variet = Q(title__contains=recherche)
        for o in search:
            tmp_categ = Q(title__contains=o) | Q(url__contains=o)
            req_categ = req_categ | tmp_categ
            
            tmp_variet = Q(title__contains=o) | Q(latin__contains=o) | Q(url__contains=o)
            req_variet = req_variet | tmp_variet
        
        categories = Category.objects.filter(req_categ)
        varieties = Variety.objects.filter(req_variet)
        
        return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'tree':0, 'search':request.GET["search"], 'inventory':inventory, 'demande':demande}, content_type='text/html')
        
    else:
        return render(request, '404.html', content_type='text/html')

def category_detail(request, categ):
    try:
        category = Category.objects.get(url=categ)
        if request.user.username:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group=="user":
                varieties_ids = Catalog.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
                inventory = Variety.objects.filter(pk__in=varieties_ids)
                varieties_ids = Desire.objects.filter(user=User.objects.get(username=request.user.username)).values_list('variety', flat=True)
                demande = Variety.objects.filter(pk__in=varieties_ids)
            else:
                varieties_ids = Catalog_group.objects.filter(group=Group.objects.get(pk=group)).values_list('variety', flat=True)
                inventory = Variety.objects.filter(pk__in=varieties_ids)
                varieties_ids = Desire_group.objects.filter(group=Group.objects.get(pk=group)).values_list('variety', flat=True)
                demande = Variety.objects.filter(pk__in=varieties_ids)
        else:
            inventory = 0
            demande = 0
        nom_page = category.title
        url_page = category.url

        descendant = category.get_descendants(include_self=False)
        ascendants = category.get_ancestors(ascending=False, include_self=False)
        
        categories = category.get_children()
        
        if not descendant:
            varieties = Variety.objects.filter(category__url=categ)
        else:
            varieties = Variety.objects.filter(category__in=descendant)
        
        return render(request, 'category_list.html', {'categories': categories, 'varieties': varieties, 'cat_parents':ascendants, 'nom_page':nom_page, 'url_page':url_page, 'inventory':inventory, 'demande':demande, 'tree':1}, content_type='text/html')

    except:
        return render(request, '404.html', content_type='text/html')

def add_category(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = AddCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = AddCategoryForm()
        return render(request, 'add_category.html', {'form' : form}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')


class VarietyResultJson(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Variety.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
