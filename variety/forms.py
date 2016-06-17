# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms

from variety.models import *

class AddVarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        fields = ['title', 'latin', 'category', 'is_stock']
        labels = {
            'title':"Nom",
            'latin':"Nom latin",
            'category':"Category",
            'is_stock':"En stock",
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']

        if Variety.objects.filter(title=title).exists():
            raise forms.ValidationError(u"Le nom de cette category existe déjà")
        return title
    
    def save(self):
        cleaned_data = super(AddVarietyForm, self).clean()
        new_Category = Category.objects.create(
                title = cleaned_data['title'],
                url = slugify(cleaned_data['title']),
                latin = cleaned_data['latin'],
                category = cleaned_data['category'],
                is_stock = cleaned_data['is_stock'],
            )
        new_Category.save() 
        
class VarietyInventoryForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['user', 'variety', 'qtt', 'shares_qtt']
        labels = {
            'variety':"Variétée",
            'qtt':"Quantitée",
            'shares_qtt':"Quantitée partageable",
        }
        widgets = {
            'user': forms.HiddenInput(),
        }
        
    def clean(self):
        cleaned_data = super(VarietyInventoryForm, self).clean()
        if cleaned_data['qtt'] < cleaned_data['shares_qtt']:
            self.add_error("qtt", u"Vous devez avoir plus d'éléments en stock que ceux que vous mettez à disposition.")
        if Catalog.objects.filter(variety=cleaned_data['variety']).exists():
            self.add_error("variety", u"Vous possédez déjà de cette variétée.")
        return cleaned_data

class VarietyRequestForm(forms.ModelForm):
    class Meta:
        model = Desire
        fields = ['user', 'variety', 'qtt', 'message']
        labels = {
            'variety':"Variétée",
            'qtt':"Quantitée",
            'message':"Message",
        }
        widgets = {
            'user': forms.HiddenInput(),
            'message': forms.Textarea,
        }
        
    def clean(self):
        cleaned_data = super(VarietyRequestForm, self).clean()
        if Desire.objects.filter(variety=cleaned_data['variety']).exists():
            self.add_error("variety", u"Vous demandez déjà de cette variétée.")
        return cleaned_data