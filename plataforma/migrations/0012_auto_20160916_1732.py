# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0011_auto_20160916_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='status',
            new_name='activar',
        ),
    ]
