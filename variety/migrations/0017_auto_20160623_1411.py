# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0016_auto_20160622_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
