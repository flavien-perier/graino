# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0014_auto_20160621_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='adress',
            new_name='address',
        ),
    ]
