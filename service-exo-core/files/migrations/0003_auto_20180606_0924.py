# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-06 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_uploadedfile_uploadedfileversion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedfileversion',
            old_name='resource',
            new_name='uploaded_file',
        ),
    ]
