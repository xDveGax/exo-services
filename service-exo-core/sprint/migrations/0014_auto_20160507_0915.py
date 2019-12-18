# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-07 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0013_auto_20160422_0628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={
                'ordering': ['name'], 'permissions': (
                    ('team_full_view', 'Team included'), ('coach_team', 'Team coach'), (
                        'team_delete_exoproject', 'Team: Delete ExO Project',
                    ), ('can_create_task', 'Team: Add task'),
                ), 'verbose_name': 'Team', 'verbose_name_plural': 'Teams',
            },
        ),
    ]
