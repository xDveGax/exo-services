# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 15:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
from django.contrib.auth.models import Group


def create_registration_group(apps, schema_editor):
    Group.objects.get_or_create(
        name=settings.REGISTRATION_GROUP_NAME,
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultant', '__first__'),
    ]

    operations = [
        migrations.RunPython(
            code=create_registration_group,
        ),
    ]
