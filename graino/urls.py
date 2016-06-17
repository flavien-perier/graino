# -*- coding: utf-8 -*-

# Graino view
from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from graino.views import *
from variety.views import *
from category.views import *
from account.views import *

# import autocomplete_light
# autocomplete_light.autodiscover()
# admin.autodiscover()

# Graino urls


urlpatterns = [
    # url(r'^autocomplete/', include('autocomplete_light.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html'), name='user_profile'),
    
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aide/$', aide, name='aide'),
    
    url('^', include('variety.urls')),
    url('^', include('category.urls')),
    url('^', include('account.urls')),
]
