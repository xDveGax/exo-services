# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-21 12:04
from __future__ import unicode_literals

from django.db import migrations

from utils.groups import GROUPS


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group_name in GROUPS:
        Group.objects.get_or_create(name=group_name)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0003_auto_20160923_0909'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
