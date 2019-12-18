# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import autoslug.fields
import utils.mixins.location_timezone_mixin
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
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
                ('name', models.CharField(max_length=200)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                (
                    'slug', autoslug.fields.AutoSlugField(
                        editable=False, null=True, populate_from='name', unique=True),
                ),
                (
                    'status', models.CharField(
                        choices=[
                            ('W', 'Not Started'), ('D', 'Draft'),
                            ('S', 'In progress'), ('F', 'Finished'),
                        ], default='D', max_length=1,
                    ),
                ),
                ('agenda', models.URLField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('lapse', models.CharField(blank=True, choices=[
                 ('W', 'Week'), ('D', 'Day')], max_length=1, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('place_id', models.CharField(blank=True, max_length=255, null=True)),
                ('template', models.CharField(blank=True, default='', max_length=100,
                                              null=True, verbose_name='Template or project type')),
                ('category', models.CharField(choices=[('T', 'Training'), ('C', 'Certification'),
                                                       ('D', 'Demo'), ('E', 'Event'), ('M', 'Transformation')], default='M', max_length=1),),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True),),
                ('comment', models.TextField(blank=True, null=True)),
                ('timezone', utils.mixins.location_timezone_mixin.TimeZoneField(blank=True, null=True))
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
