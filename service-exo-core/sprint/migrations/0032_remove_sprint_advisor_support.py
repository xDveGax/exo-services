# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0031_sprint_advisor_support'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='advisor_support',
        ),
    ]
