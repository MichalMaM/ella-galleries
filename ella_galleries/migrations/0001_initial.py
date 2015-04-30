# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import app_data.fields
import ella.core.cache.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('core', '0002_auto_20150430_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('publishable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Publishable')),
                ('content', models.TextField(verbose_name='Content', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
            bases=('core.publishable',),
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+$'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')], max_length=255, blank=True, null=True, verbose_name='Slug')),
                ('order', models.IntegerField(verbose_name='Object order')),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('text', models.TextField(blank=True)),
                ('app_data', app_data.fields.AppDataField(default=b'{}', editable=False)),
                ('gallery', ella.core.cache.fields.CachedForeignKey(verbose_name='Parent gallery', to='ella_galleries.Gallery')),
                ('photo', ella.core.cache.fields.CachedForeignKey(verbose_name='Photo', blank=True, to='photos.Photo', null=True)),
            ],
            options={
                'verbose_name': 'Gallery item',
                'verbose_name_plural': 'Gallery items',
            },
        ),
    ]
