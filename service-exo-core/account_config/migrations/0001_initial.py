# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-04 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=80, verbose_name='parameter name')),
                ('param_type', models.CharField(choices=[('bool', 'boolean'),
                                                         ('int', 'integer')], max_length=80, verbose_name='parameter type')),
                ('_default_value', models.CharField(max_length=80, verbose_name='default value')),
                ('group', models.CharField(choices=[('ask_to_ecosystem', 'Ask to Ecosystem'), ('team_communication', 'Team Communication'), (
                    'swarm_sessions', 'Swarm Sessions'), ('cicles', 'Circles'), ('opportunities', 'Opportunities')], max_length=80, verbose_name='configuration group')),
                ('condition_for_available', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_value', models.CharField(max_length=80, verbose_name='value')),
                ('config_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                       related_name='values', to='account_config.ConfigParam', verbose_name='config parameter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='config_values', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Config value',
                'verbose_name_plural': 'Config values',
            },
        ),
        migrations.AddField(
            model_name='configparam',
            name='user',
            field=models.ManyToManyField(
                related_name='config_params', through='account_config.ConfigValue', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterUniqueTogether(
            name='configvalue',
            unique_together={('user', 'config_parameter')},
        ),
        migrations.AlterUniqueTogether(
            name='configparam',
            unique_together={('name', 'group')},
        ),
    ]
