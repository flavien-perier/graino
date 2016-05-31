# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0004_auto_load_fixtures_categories_20151027_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(max_length=250, default=datetime.datetime(2016, 5, 31, 8, 53, 38, 897793, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
