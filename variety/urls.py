# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# Variety urls


urlpatterns = [
    #url(r'^update/$', update, name='update'),
    url(r'^add/varieties/$', add_variety, name='add_variety'),
    url(r'^add/varieties/(?P<categ>[\w-]+)$', add_variety_details, name='add_variety_details'),
    
    url(r'^varieties_inventory/$', variety_inventory, name='variety_inventory'),
    url(r'^add/varieties_inventory/(?P<categ>[\w-]+)$', variety_inventory_add, name='variety_inventory_add'),
    url(r'^delete/confirmation/varieties_inventory/(?P<categ>[\w-]+)$', variety_inventory_delete_confirmation, name='variety_inventory_delete'),
    url(r'^delete/varieties_inventory/(?P<categ>[\w-]+)$', variety_inventory_delete, name='variety_inventory_delete'),
    
    url(r'^varieties_request/$', variety_request, name='variety_request'),
    url(r'^add/varieties_request/(?P<categ>[\w-]+)$', variety_request_add, name='variety_request_add'),
    url(r'^delete/confirmation/varieties_request/(?P<categ>[\w-]+)$', variety_request_delete_confirmation, name='variety_request_delete'),
    url(r'^delete/varieties_request/(?P<categ>[\w-]+)$', variety_request_delete, name='variety_request_delete'),
]