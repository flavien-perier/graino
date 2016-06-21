# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *
from group.views import *

# Account urls


urlpatterns = [
    url(r'^create_account/$', create_account, name='create_account'),
    url(r'^me/$', me, name='me'),
    url(r'^me/edit/$', me_edit, name='me_edit'),
    url(r'^user_list/$', user_list, name='user_list'),
]