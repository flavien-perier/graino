# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms
from pygeocoder import Geocoder

from variety.models import *

class CreationUserForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail", max_length=100)
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(), max_length=100)
    password2 = forms.CharField(label="Retapez le mot de passe", widget=forms.PasswordInput(), max_length=100)
    
    def clean(self):
        cleaned_data = super(CreationUserForm, self).clean()
        user_name = cleaned_data.get('username')
        user_mail = cleaned_data.get('email')
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error("password", "Les deux mot de passe sont différents.")
        
        if User.objects.filter(username=user_name).exists():
            self.add_error("username", "Le nom d'utilisateur est déjà pris.")
            
        if User.objects.filter(email=user_mail).exists():
            self.add_error("email", "Cette adresse e-mail est déjà utilisée.")
        return cleaned_data
    
    def save(self):
        cleaned_data = super(CreationUserForm, self).clean()
        new_user = User.objects.create(
                username = cleaned_data['username'],
                password = cleaned_data['password'],
                email = cleaned_data['email']
            )
        new_user.save()
        new_profile = Profile.objects.create(
                user = User.objects.get(username=cleaned_data['username'])
            )
        new_profile.save()
        
class EditionUserForm_user(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', ] 
        
    
    def clean(self):
        cleaned_data = super(EditionUserForm_user, self).clean()
        user_mail = cleaned_data.get('email')

        if User.objects.filter(email=user_mail).exists() and User.objects.get(email=user_mail).email != self.instance.email:
            self.add_error("email", "Cette adresse e-mail est déjà utilisée.")
        return cleaned_data
        
        
class EditionUserForm_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'address', 'zip_code', 'lt', 'lg']
        labels = {
            'country':"Pays",
            'city':"Ville",
            'address':"Adresse",
            'zip_code':"Code postale",
            'lt':"Latitude",
            'lg':"Longitude",
        }
        
    def save(self):
        cleaned_data = super(EditionUserForm_profile, self).clean()
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
