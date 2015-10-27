# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0002_auto_20151022_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='latin',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='category',
            field=mptt.fields.TreeForeignKey(to='variety.Category'),
        ),
    ]
