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

from .forms import CreationGroupForm, EditionGroupForm

import unicodedata

# group view

def create_group(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = CreationGroupForm(data=request.POST)
            if form.is_valid():
                form.save()
                User_group.objects.create(
                    user = User.objects.get(username = request.user.username),
                    group = Group.objects.get(title = request.POST['title']),
                    rank = 2,
                )
                User_group.save
                return HttpResponseRedirect('/group/list/')
        else:
            form = CreationGroupForm()
        return render(request, 'create_group.html', {'form' : form}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def group_edit(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['id']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['id']).rank == 2:
            group_infos = Group.objects.get(pk=request.GET['id'])
            if request.method == "POST":
                form = EditionGroupForm(data=request.POST, instance=group_infos)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/group/list/')
            else:
                form = EditionGroupForm(instance=group_infos)

            return render(request, 'edit_group.html', {'form' : form}, content_type='text/html')
        else:
            return render(request, '403.html', content_type='text/html')
    except:
        return render(request, '404.html', content_type='text/html')

def group_list(request):
    if request.user.is_authenticated():
        groups = Group.objects.all()
        user_group = Group.objects.filter(pk__in=User_group.objects.filter(rank=2).values_list('group', flat=True) )
        return render(request, 'group_list.html', {'groups':groups, 'user_group':user_group}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')

def group_delete_confirmation(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['id']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['id']).rank == 2:
            return render(request, 'group_delete.html', {"url":request.GET['id']}, content_type='text/html')
        else:
            return render(request, '403.html', content_type='text/html')
    except:
        return render(request, '404.html', content_type='text/html')

def group_delete(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['id']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['id']).rank == 2:
            delete_request = Group.objects.filter(pk=request.GET['id'])
            delete_request.delete()

            return HttpResponseRedirect("/group/list/")
        else:
            return render(request, '403.html', content_type='text/html')
    except:
         return render(request, '404.html', content_type='text/html')

def group_add_user(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['id']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['id']).rank >= 1:
            if request.method == 'POST' and User_group.objects.filter(user__username=request.POST["user"]).filter(group=request.GET['id']).exists() == 0:
                try:
                    add_user = User_group.objects.create(
                            user = User.objects.get(username = request.POST["user"]),
                            group = Group.objects.get(pk = request.GET['id']),
                            rank = request.POST["rank"],
                        )
                    add_user.save
                    message = "Utilisatuer ajouter"
                except:
                    message = "Utilisateur non trouver ou déjà présent."
            else:
                message = ""
            return render(request, 'group_add_user.html', {"message":message}, content_type='text/html')
        else:
            return render(request, '403.html', content_type='text/html')
    except:
         return render(request, '404.html', content_type='text/html')

def group_user_list(request):
    try:
        if request.user.is_authenticated():
            url = request.GET["id"]
            users = User_group.objects.filter(group = url)
            rank = users.get(user__username=request.user.username).rank
            return render(request, 'group_user_list.html', {'users':users, 'url':url, 'rank':rank}, content_type='text/html')
        else:
            return render(request, '403.html', content_type='text/html')
    except:
         return render(request, '404.html', content_type='text/html')

def group_user_delete_confirmation(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['group']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['group']).rank == 2:
            return render(request, 'group_user_delete.html', {"group":request.GET['group'], "user":request.GET['user']}, content_type='text/html')
        else:
            return render(request, '403.html', content_type='text/html')
    except:
        return render(request, '404.html', content_type='text/html')

def group_user_delete(request):
    try:
        if request.user.is_authenticated() and User_group.objects.filter(user__username=request.user.username).filter(group=request.GET['group']).exists() and User_group.objects.filter(user__username=request.user.username).get(group=request.GET['group']).rank == 2:
            delete_request = User_group.objects.filter(group=request.GET['group']).filter(user=request.GET['user'])
            delete_request.delete()

            return HttpResponseRedirect("/group/user/list/?id="+request.GET['group'])
        else:
            return render(request, '403.html', content_type='text/html')
    except:
        return render(request, '404.html', content_type='text/html')

def group_choice(request):
    if request.method == "POST":
        request.session["group"] = request.POST["group"]
    groups = User_group.objects.filter(user__username=request.user.username)
    try:
        actu = request.session["group"]
    except:
        actu = "user"
    return render(request, 'group_choice.html', {'groups':groups, 'actu':actu}, content_type='text/html')