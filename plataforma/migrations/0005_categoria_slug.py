# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_auto_20160912_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
