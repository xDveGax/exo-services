# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-16 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exo_activity', '0001_squashed_0007_auto_20171215_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='exoactivity',
            name='require_certification',
            field=models.BooleanField(default=False),
        ),
    ]
