# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.text import slugify

from variety.models import *
 
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent', 'illustration']
        labels = {
            'title':"Nom",
            'illustration':"Image",
            'parent':"Parent",
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']

        if Category.objects.filter(title=title).exists():
            raise forms.ValidationError(u"Le nom de cette category existe déjà")
        return title
    
    def save(self):
        cleaned_data = super(AddCategoryForm, self).clean()
        new_Category = Variety.objects.create(
                title = cleaned_data['title'],
                url = slugify(cleaned_data['title']),
                parent = cleaned_data['parent'],
                illustration = cleaned_data['illustration']
            )
        new_Category.save()
