# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 05:29
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('plataforma', '0020_articulo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]