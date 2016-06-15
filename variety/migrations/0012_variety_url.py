# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0011_auto_20160610_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='url',
            field=models.SlugField(default=datetime.datetime(2016, 6, 14, 12, 45, 17, 801982, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
