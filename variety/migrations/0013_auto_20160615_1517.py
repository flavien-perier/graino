# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0012_variety_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='message',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
