# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import os
from sys import path
from django.core import serializers


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../fixtures'))
fixture_filename = 'categories.json'


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("variety", "Category")
    MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0003_auto_20151023_2210'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
