# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0010_auto_20160609_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='addrdess',
            new_name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='lg',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lt',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='illustration',
            field=models.ImageField(null=True, upload_to=b'media/', blank=True),
        ),
    ]
