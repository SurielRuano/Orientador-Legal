# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_categoria_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]