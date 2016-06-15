# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0009_auto_20160606_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adrdess',
            new_name='addrdess',
        ),
    ]
