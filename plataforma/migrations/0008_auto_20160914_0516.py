# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_auto_20160913_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ManyToManyField(related_name='articulos', to='plataforma.Categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='colaborador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='plataforma.Colaborador'),
        ),
    ]
