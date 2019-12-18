# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        # ('project', '0039_auto_20170405_1436'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('zoom_project', '0004_auto_20161027_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoomRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created', model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='created',
                    ),
                ),
                (
                    'modified', model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='modified',
                    ),
                ),
                ('object_id', models.PositiveIntegerField()),
                ('meeting_id', models.CharField(max_length=256, verbose_name='Meeting ID (Zoom)')),
                ('host_meeting_id', models.CharField(max_length=256, verbose_name='Host Meeting ID (Zoom)')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Zoom Room',
                'verbose_name_plural': 'Zoom Rooms',
            },
        ),
        migrations.CreateModel(
            name='ZoomSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'created', model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='created',
                    ),
                ),
                (
                    'modified', model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name='modified',
                    ),
                ),
                ('zoom_api_key', models.CharField(max_length=256)),
                ('zoom_secret_key', models.CharField(max_length=256)),
                (
                    'project', models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='zoom_settings', to='project.Project',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Zoom Settings',
                'verbose_name_plural': 'Zooms Settings',
            },
        ),
        migrations.AddField(
            model_name='zoomroom',
            name='settings',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='rooms', to='zoom_project.ZoomSettings',
            ),
        ),
    ]
