# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variety', '0006_auto_20160602_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='shares_qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catalog_group',
            name='qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='catalog_group',
            name='shares_qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='desire',
            name='qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='desire_group',
            name='qtt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_group',
            name='rank',
            field=models.IntegerField(),
        ),
    ]
