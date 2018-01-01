# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='big_image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='small_image',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
