# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-05-17 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0006_merge_20180911_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
