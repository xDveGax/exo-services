# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 11:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0003_auto_20171214_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='userreward',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
