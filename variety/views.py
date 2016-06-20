# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

from .forms import AddVarietyForm, VarietyInventoryForm, VarietyInventoryUpdateForm, VarietyRequestForm, VarietyRequestUpdateForm

import time

# Variety view


def update(request):
    """for o in Category.objects.all():
        o.url = slugify(o.title)
        o.save()"""
    for o in Variety.objects.all():
        o.url = slugify(o.title)
        o.save()
        
def add_variety(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = AddVarietyForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = AddVarietyForm()
            
        return render(request, 'add_variety.html', {'form' : form}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def add_variety_details(request, categ):
    if request.user.is_authenticated():
        try:
            if request.method == "POST":
                form = AddVarietyForm(request.POST, initial={'category': Variety.objects.get(url=categ).category})
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/')
            else:
                form = AddVarietyForm(initial={'category': Category.objects.get(url=categ)})
                
            return render(request, 'add_variety.html', {'form' : form}, content_type='text/html')
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_inventory(request, categ=0):
    if request.user.is_authenticated():
        varieties = Catalog.objects.filter(user__username=request.user.username)
        
        if request.method == "POST":
            print (request.POST["variety"])
            form = VarietyInventoryForm(request.POST, initial={'user': User.objects.get(username=request.user.username)})
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/varieties_inventory/')
        else:
            form = VarietyInventoryForm(initial={'user': User.objects.get(username=request.user.username), 'qtt':'1', 'shares_qtt':1})
            
        return render(request, 'variety_inventory.html', {'form' : form, 'varieties' : varieties}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_inventory_add(request, categ):
    if request.user.is_authenticated():
        try:
            new_inventory = Catalog.objects.create(
                    user = User.objects.get(username=request.user.username),
                    variety = Variety.objects.get(url=categ),
                    qtt = 1,
                    shares_qtt = 1,
                )
            new_inventory.save()

            return HttpResponseRedirect(request.META["HTTP_REFERER"])
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_inventory_delete_confirmation(request, categ):
    if request.user.is_authenticated():
        return render(request, 'variety_inventory_delete.html', {"url":categ}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_inventory_delete(request, categ):
    if request.user.is_authenticated():
        try:
            delete_inventory = Catalog.objects.filter(user = User.objects.get(username=request.user.username)).filter(variety__url = categ)
            delete_inventory.delete()

            return HttpResponseRedirect("/varieties_inventory/")
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_inventory_update(request, categ):
    if request.user.is_authenticated():
        try:
            variet = Catalog.objects.filter(user__username=request.user.username).get(variety__url=categ)
            
            if request.method == "POST":
                form = VarietyInventoryUpdateForm(data=request.POST, instance=variet)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/varieties_inventory/')
            else:        
                form = VarietyInventoryUpdateForm(instance=variet)
                
            return render(request, 'variety_inventory_update.html', {'form':form, 'title':variet.variety.title}, content_type='text/html')
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_request(request, categ=0):
    if request.user.is_authenticated():
        varieties = Desire.objects.filter(user__username=request.user.username)
        
        if request.method == "POST":
            print (request.POST["variety"])
            form = VarietyRequestForm(request.POST, initial={'user': User.objects.get(username=request.user.username)})
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/varieties_request/')
        else:
            form = VarietyRequestForm(initial={'user': User.objects.get(username=request.user.username), 'qtt':'1', 'shares_qtt':1})
            
        return render(request, 'variety_request.html', {'form' : form, 'varieties' : varieties}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_request_add(request, categ):
    if request.user.is_authenticated():
        try:
            new_request = Desire.objects.create(
                    user = User.objects.get(username=request.user.username),
                    variety = Variety.objects.get(url=categ),
                    qtt = 1,
                )
            new_request.save()
            
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_request_delete_confirmation(request, categ):
    if request.user.is_authenticated():
        return render(request, 'variety_request_delete.html', {"url":categ}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_request_delete(request, categ):
    if request.user.is_authenticated():
        try:
            delete_request = Desire.objects.filter(user = User.objects.get(username=request.user.username)).filter(variety__url = categ)
            delete_request.delete()

            return HttpResponseRedirect("/varieties_request/")
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_request_update(request, categ):
    if request.user.is_authenticated():
        try:
            variet = Desire.objects.filter(user__username=request.user.username).get(variety__url=categ)
            
            if request.method == "POST":
                form = VarietyRequestUpdateForm(data=request.POST, instance=variet)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/varieties_request/')
            else:        
                form = VarietyRequestUpdateForm(instance=variet)
                
            return render(request, 'variety_request_update.html', {'form' : form, 'title':variet.variety.title}, content_type='text/html')
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')