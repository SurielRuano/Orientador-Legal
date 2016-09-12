# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 04:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='colaboradores/%Y/%m')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudColaboracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('licenciatura_leyes', models.CharField(choices=[('si', 'Si'), ('no', 'No')], max_length=2)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_solicitud', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
