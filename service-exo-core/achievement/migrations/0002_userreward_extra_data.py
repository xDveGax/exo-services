# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 11:03
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreward',
            name='extra_data',
            field=django.contrib.postgres.fields.hstore.HStoreField(default={}),
            preserve_default=False,
        ),
    ]
