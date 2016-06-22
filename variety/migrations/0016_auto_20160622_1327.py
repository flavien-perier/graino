# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0015_auto_20160621_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire_group',
            name='message',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
