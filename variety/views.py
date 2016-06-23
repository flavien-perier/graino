# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView 
from django.utils import timezone 
from django import forms 
from django.utils.text import slugify
 
from django.http import HttpResponse 
from django.shortcuts import render_to_response

from variety.models import *

from .forms import AddVarietyForm, VarietyInventoryForm, VarietyInventoryForm_group, VarietyInventoryUpdateForm, VarietyInventoryUpdateForm_group, VarietyRequestForm, VarietyRequestForm_group, VarietyRequestUpdateForm, VarietyRequestUpdateForm_group

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
        try:
            group = request.session["group"]
        except:
            group = "user"
        
        if group == "user":
            varieties = Catalog.objects.filter(user__username=request.user.username)
        else:
            varieties = Catalog_group.objects.filter(group=group)
        
        if request.method == "POST":
            if group == "user":
                form = VarietyInventoryForm(request.POST, initial={'user':User.objects.get(username=request.user.username)})
            else:
                form = VarietyInventoryForm_group(request.POST, initial={'group':group})
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/varieties_inventory/')
        else:
            if group == "user":
                form = VarietyInventoryForm(initial={'user':User.objects.get(username=request.user.username), 'qtt':'1', 'shares_qtt':1})
            else:
                form = VarietyInventoryForm_group(initial={'group':group, 'qtt':'1', 'shares_qtt':1})
            
        return render(request, 'variety_inventory.html', {'form' : form, 'varieties' : varieties}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_inventory_add(request, categ):
    if request.user.is_authenticated():
        try:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group == "user":
                new_inventory = Catalog.objects.create(
                        user = User.objects.get(username=request.user.username),
                        variety = Variety.objects.get(url=categ),
                        qtt = 1,
                        shares_qtt = 1,
                    )
            else:
                new_inventory = Catalog_group.objects.create(
                        group = Group.objects.get(pk=group),
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
            try:
                group = request.session["group"]
            except:
                group = "user"
            if group=="user":
                delete_inventory = Catalog.objects.filter(user = User.objects.get(username=request.user.username)).filter(variety__url=categ)
            else:
                delete_inventory = Catalog_group.objects.filter(group=group).filter(variety__url=categ)
            delete_inventory.delete()

            return HttpResponseRedirect("/varieties_inventory/")
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_inventory_update(request, categ):
    if request.user.is_authenticated():
        try:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group == "user":
                variet = Catalog.objects.filter(user__username=request.user.username).get(variety__url=categ)
            else:
                variet = Catalog_group.objects.filter(group=group).get(variety__url=categ)
            
            if request.method == "POST":
                if group == "user":
                    form = VarietyInventoryUpdateForm(data=request.POST, instance=variet)
                else:
                    form = VarietyInventoryUpdateForm_group(data=request.POST, instance=variet)
                
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/varieties_inventory/')
            else:
                if group == "user":
                    form = VarietyInventoryUpdateForm(instance=variet)
                else:
                    form = VarietyInventoryUpdateForm_group(instance=variet)
                
            return render(request, 'variety_inventory_update.html', {'form':form, 'title':variet.variety.title}, content_type='text/html')
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_request(request, categ=0):
    if request.user.is_authenticated():
        try:
            group = request.session["group"]
        except:
            group = "user"
        
        if group == "user":
            varieties = Desire.objects.filter(user__username=request.user.username)
        else:
            varieties = Desire_group.objects.filter(group=group)

        if request.method == "POST":
            if group == "user":
                form = VarietyRequestForm(request.POST, initial={'user':User.objects.get(username=request.user.username)})
            else:
                form = VarietyRequestForm_group(request.POST, initial={'group':group})
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/varieties_request/')
        else:
            if group == "user":
                form = VarietyRequestForm(initial={'user':User.objects.get(username=request.user.username), 'qtt':'1', 'shares_qtt':1})
            else:
                form = VarietyRequestForm_group(initial={'group':group, 'qtt':'1', 'shares_qtt':1})
            
        return render(request, 'variety_request.html', {'form' : form, 'varieties' : varieties}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
    
def variety_request_add(request, categ):
    if request.user.is_authenticated():
        try:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group == "user":
                new_request = Desire.objects.create(
                        user = User.objects.get(username=request.user.username),
                        variety = Variety.objects.get(url=categ),
                        qtt = 1,
                    )
            else:
                new_request = Desire_group.objects.create(
                        group = Group.objects.get(pk=group),
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
            try:
                group = request.session["group"]
            except:
                group = "user"
            if group=="user":
                delete_request = Desire.objects.filter(user = User.objects.get(username=request.user.username)).filter(variety__url=categ)
            else:
                delete_request = Desire_group.objects.filter(group=group).filter(variety__url=categ)
            delete_request.delete()

            return HttpResponseRedirect("/varieties_request/")
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def variety_request_update(request, categ):
    if request.user.is_authenticated():
        try:
            try:
                group = request.session["group"]
            except:
                group = "user"
            
            if group == "user":
                variet = Desire.objects.filter(user__username=request.user.username).get(variety__url=categ)
            else:
                variet = Desire_group.objects.filter(group=group).get(variety__url=categ)
            
            if request.method == "POST":
                if group == "user":
                    form = VarietyRequestUpdateForm(data=request.POST, instance=variet)
                else:
                    form = VarietyRequestUpdateForm_group(data=request.POST, instance=variet)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/varieties_request/')
            else:
                if group == "user":
                    form = VarietyRequestUpdateForm(instance=variet)
                else:
                    form = VarietyRequestUpdateForm_group(instance=variet)
                
            return render(request, 'variety_request_update.html', {'form' : form, 'title':variet.variety.title}, content_type='text/html')
        except:
            return render(request, '404.html', content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def varieties_inventory_public(request, type, id):
    #try:
    if type=="user":
        varieties = Catalog.objects.filter(user=Profile.objects.get(code=id).user)
        user = Profile.objects.get(code=id).user.username
    elif type=="group":
        varieties = Catalog_group.objects.filter(group__code=id)
        user = Group.objects.get(code=id).title
    else:
        return render(request, '404.html', content_type='text/html')

    return render(request, 'variety_inventory_public.html', {'varieties':varieties, 'user':user}, content_type='text/html')
    """except:
        return render(request, '404.html', content_type='text/html')"""