# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-28 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0059_auto_20180322_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultantexoprofile',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
