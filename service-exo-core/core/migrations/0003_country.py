# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-05 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180821_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('native_name', models.CharField(db_index=True, max_length=255)),
                ('code_2', models.CharField(db_index=True, max_length=2, unique=True)),
                ('code_3', models.CharField(db_index=True, max_length=3, unique=True)),
                ('flag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
