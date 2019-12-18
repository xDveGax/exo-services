# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_project', '0012_zoomsettings_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zoomsettings',
            name='rooms',
        ),
        migrations.AddField(
            model_name='zoomroom',
            name='_zoom_settings',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='rooms', to='zoom_project.ZoomSettings',
            ),
        ),
    ]
