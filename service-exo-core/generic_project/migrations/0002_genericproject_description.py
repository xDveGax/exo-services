# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-06 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericproject',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
