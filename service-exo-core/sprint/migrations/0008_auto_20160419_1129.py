# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0007_exoproject_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={
                'permissions': (
                    ('full_view', 'Team included'), ('coach_team', 'Team coach'), (
                        'team_list_exoproject',
                        'List Team: ExO Project',
                    ),
                ), 'verbose_name': 'Sprint Team', 'verbose_name_plural': 'Sprints Teams',
            },
        ),
    ]
