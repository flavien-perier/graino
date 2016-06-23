# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms
from pygeocoder import Geocoder

from variety.models import *

import random

class CreationGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['title', 'code', 'country', 'city', 'address', 'zip_code', 'lg', 'lt'] 
        labels = {
            'title':"Nom",
            'country':"Pays",
            'city':"Ville",
            'address':"Adresse",
            'zip_code':"Code postale",
            'lg':"Longitude",
            'lt':"Latitude",
        }
        widgets = {
            'code': forms.HiddenInput(),
        }
    
    def save(self):
        cleaned_data = super(CreationGroupForm, self).clean()
        if (not cleaned_data['lt'] or not cleaned_data['lg']) and (cleaned_data['address'] and cleaned_data['zip_code'] and cleaned_data['city']):
            try:
                results = Geocoder.geocode('%s %s %s' % (cleaned_data['address'], cleaned_data['zip_code'], cleaned_data['city']))
                self.instance.lt = results[0].coordinates[0]
                self.instance.lg = results[0].coordinates[1]
            except GeocoderError:
                pass
        
        self.instance.title = cleaned_data['title']
        self.instance.code = random.randrange(0, 999999999999999, 3)
        self.instance.country = cleaned_data['country']
        self.instance.city = cleaned_data['city']
        self.instance.address = cleaned_data['address']
        self.instance.zip_code = cleaned_data['zip_code']
        self.instance.save()

class EditionGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['country', 'city', 'address', 'zip_code', 'lg', 'lt'] 
        labels = {
            'country':"Pays",
            'city':"Ville",
            'address':"Adresse",
            'zip_code':"Code postale",
            'lg':"Longitude",
            'lt':"Latitude",
        }
    
    def save(self):
        cleaned_data = super(EditionGroupForm, self).clean()
        if (not cleaned_data['lt'] or not cleaned_data['lg']) and (cleaned_data['address'] and cleaned_data['zip_code'] and cleaned_data['city']):
            try:
                results = Geocoder.geocode('%s %s %s' % (cleaned_data['address'], cleaned_data['zip_code'], cleaned_data['city']))
                self.instance.lt = results[0].coordinates[0]
                self.instance.lg = results[0].coordinates[1]
            except GeocoderError:
                pass
        
        self.instance.country = cleaned_data['country']
        self.instance.city = cleaned_data['city']
        self.instance.address = cleaned_data['address']
        self.instance.zip_code = cleaned_data['zip_code']
        self.instance.save()