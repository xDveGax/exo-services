# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-19 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0003_load_attributes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circle',
            options={'ordering': ['name'], 'permissions': (
                ('create_post', 'Create post'),), 'verbose_name': 'Circle', 'verbose_name_plural': 'Circle'},
        ),
        migrations.AddField(
            model_name='circle',
            name='code',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
