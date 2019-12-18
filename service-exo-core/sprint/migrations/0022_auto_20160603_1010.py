# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-03 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0021_auto_20160602_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='sprint_team_related', to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
