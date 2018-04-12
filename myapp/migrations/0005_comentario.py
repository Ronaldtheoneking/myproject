# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180208_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Articulo')),
            ],
        ),
    ]
