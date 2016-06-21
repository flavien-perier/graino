# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0013_auto_20160615_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='lg',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='group',
            name='lt',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
    ]
