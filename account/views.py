# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group
from django.forms import ModelForm, inlineformset_factory, BaseModelFormSet, modelformset_factory

from variety.models import *
from .forms import CreationUserForm, EditionUserForm_user, EditionUserForm_profile

# Account view

def create_account(request):
    if request.method == "POST":
        form = CreationUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreationUserForm()

    return render(request, 'registration/create_account.html', {'form' : form}, content_type='text/html')

def me(request):
    if request.user.is_authenticated():
        user_infos = User.objects.get(username=request.user.username)
        profile_infos = Profile.objects.get(user__username=request.user.username)
        return render(request, 'me.html', {'user': user_infos, 'profile': profile_infos}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
        
def me_edit(request):
    if request.user.is_authenticated():
        user_infos = User.objects.get(username=request.user.username)
        profile_infos = Profile.objects.get(user__username=request.user.username)
        
        if request.method == "POST":
            form1 = EditionUserForm_user(data=request.POST, instance=user_infos, prefix="a")
            form2 = EditionUserForm_profile(data=request.POST, instance=profile_infos, prefix="b")
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return HttpResponseRedirect('/me')
        else:        
            form1 = EditionUserForm_user(instance=user_infos, prefix="a")
            form2 = EditionUserForm_profile(instance=profile_infos, prefix="b")
            
        return render(request, 'me_edit.html', {'form1' : form1, 'form2' : form2}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')
        
def user_list(request):
    if request.user.is_authenticated():
        users = Profile.objects.all()
        return render(request, 'user_list.html', {'users':users}, content_type='text/html')
    else:
        return render(request, '403.html', content_type='text/html')