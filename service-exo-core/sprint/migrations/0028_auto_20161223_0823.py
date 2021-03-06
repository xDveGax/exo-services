# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-23 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '0027_auto_20161212_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exoproject',
            options={
                'ordering': ['name'], 'permissions': (
                    ('edit_exoproject', 'Edit ExoProject'), ('view_exoproject', 'View ExoProject'), (
                        'list_exoproject', 'List ExoProject',
                    ),
                ), 'verbose_name': 'Initiative', 'verbose_name_plural': 'Initiatives',
            },
        ),
        migrations.AlterField(
            model_name='exoproject',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Initiative name'),
        ),
    ]
