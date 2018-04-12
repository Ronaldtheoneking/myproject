# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_articulo_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='dislike',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='likes',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
