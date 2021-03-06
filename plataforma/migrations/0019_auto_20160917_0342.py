# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0018_articulo_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='derechos',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='obligaciones',
        ),
        migrations.AddField(
            model_name='articulo',
            name='que_evitar',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='articulo',
            name='que_hacer',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='cuerpo_principal',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion_breve',
            field=models.TextField(max_length=250),
        ),
    ]
