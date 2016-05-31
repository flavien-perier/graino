"""graino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from otindexher_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from variety.views import *
from graino.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^varieties/', variety_list_view, name='variety_list_view'),
    url(r'^categories/$', category_list_view, name='category_list_view'),
    url(r'^categories/(?P<category>[\w-]+)/$', category_detail, name='category_detail'),

    url(r'^forms/', forms, name='forms'),
    url(r'^reponse/', reponse, name='reponse'),
    
    url(r'^update/', update, name='update'),
]