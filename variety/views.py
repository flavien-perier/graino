# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

from .forms import AddVarietyForm, VarietyInventoryForm

# Variety view


def update(request):
    """for o in Category.objects.all():
        o.url = slugify(o.title)
        o.save()"""
    for o in Variety.objects.all():
        o.url = slugify(o.title)
        o.save()
        
def add_variety(request):
    if request.method == "POST":
        form = AddVarietyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddVarietyForm()
        
    return render(request, 'add_variety.html', {'form' : form}, content_type='text/html')
    
def variety_inventory(request, categ=0):
    
    varieties = Catalog.objects.filter(user__username=request.user.username)
    
    if request.method == "POST":
        print (request.POST["variety"])
        form = VarietyInventoryForm(request.POST, initial={'user': User.objects.get(username=request.user.username)})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/variety_inventory/')
    else:
        form = VarietyInventoryForm(initial={'user': User.objects.get(username=request.user.username), 'qtt':'1', 'shares_qtt':1})
        
    return render(request, 'variety_inventory.html', {'form' : form, 'varieties' : varieties}, content_type='text/html')
    
def variety_inventory_add(request, categ):
    try:
        new_inventory = Catalog.objects.create(
                user = User.objects.get(username=request.user.username),
                variety = Variety.objects.get(url=categ),
                qtt = 1,
                shares_qtt = 1,
            )
        new_inventory.save()
        return HttpResponseRedirect('/categories/'+Variety.objects.get(url=categ).category.url)
    except:
        return render(request, '404.html', content_type='text/html')