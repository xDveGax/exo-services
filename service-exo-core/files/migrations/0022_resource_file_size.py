# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 10:04
from __future__ import unicode_literals

from django.db import migrations
import sizefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0021_delete_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='file_size',
            field=sizefield.models.FileSizeField(blank=True, null=True),
        ),
    ]
