# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('variety', '0005_category_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('qtt', models.IntegerField(max_length=5)),
                ('shares_qtt', models.IntegerField(max_length=5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('variety', models.ForeignKey(to='variety.Variety')),
            ],
            options={
                'verbose_name_plural': 'catalog',
            },
        ),
        migrations.CreateModel(
            name='Catalog_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('qtt', models.IntegerField(max_length=5)),
                ('shares_qtt', models.IntegerField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'catalog_group',
            },
        ),
        migrations.CreateModel(
            name='Desire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('qtt', models.IntegerField(max_length=5)),
                ('message', models.CharField(max_length=5000, unique=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('variety', models.ForeignKey(to='variety.Variety')),
            ],
            options={
                'verbose_name_plural': 'desire',
            },
        ),
        migrations.CreateModel(
            name='Desire_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('qtt', models.IntegerField(max_length=5)),
                ('message', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'request_group',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(related_name='to', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='one', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'follow',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('country', models.CharField(max_length=250, null=True, blank=True)),
                ('city', models.CharField(max_length=250, null=True, blank=True)),
                ('adress', models.CharField(max_length=250, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250, null=True, blank=True)),
                ('city', models.CharField(max_length=250, null=True, blank=True)),
                ('adrdess', models.CharField(max_length=250, null=True, blank=True)),
                ('zip_code', models.PositiveSmallIntegerField(max_length=6, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'profile',
            },
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('rank', models.IntegerField(max_length=1)),
                ('group', models.ForeignKey(to='variety.Group')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user_group',
            },
        ),
        migrations.AddField(
            model_name='desire_group',
            name='group',
            field=models.ForeignKey(to='variety.Group'),
        ),
        migrations.AddField(
            model_name='desire_group',
            name='variety',
            field=models.ForeignKey(to='variety.Variety'),
        ),
        migrations.AddField(
            model_name='catalog_group',
            name='group',
            field=models.ForeignKey(to='variety.Group'),
        ),
        migrations.AddField(
            model_name='catalog_group',
            name='variety',
            field=models.ForeignKey(to='variety.Variety'),
        ),
    ]
