# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *
from group.views import *

# Group urls


urlpatterns = [
    url(r'^group/create/$', create_group, name='create_group'),
    url(r'^group/edit/$', group_edit, name='group_edit'),
    url(r'^group/list/$', group_list, name='group_list'),
    url(r'^delete/confirmation/group/$', group_delete_confirmation, name='group_delete_confirmation'),
    url(r'^delete/group/$', group_delete, name='group_delete'),
    url(r'^group/add/user/$', group_add_user, name='group_add_user'),
    url(r'^group/user/list/$', group_user_list, name='group_user_list'),
    url(r'^delete/confirmation/group/user/$', group_user_delete_confirmation, name='group_user_delete_confirmation'),
    url(r'^delete/group/user/$', group_user_delete, name='group_user_delete'),
    url(r'^group/choice/$', group_choice, name='group_choice'),
]