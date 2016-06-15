# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0008_pictures'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pictures',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='illustration',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
