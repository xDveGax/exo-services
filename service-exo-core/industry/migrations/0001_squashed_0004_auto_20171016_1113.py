# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-31 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import industry.manager
import model_utils.fields


def create_industries(apps, schema_editor):
    Industry = apps.get_model('industry', 'Industry')
    for industry_name in settings.CORE_CH_INDUSTRIES_LIST:
        industry, created = Industry.objects.get_or_create(name=industry_name)


class Migration(migrations.Migration):

    replaces = [
        ('industry', '0001_initial'), ('industry', '0002_auto_20160222_1254'),
        ('industry', '0003_auto_20170630_1202'), ('industry', '0004_auto_20171016_1113'),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
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
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Industries',
                'verbose_name': 'Industry',
                'ordering': ['name'],
            },
        ),
        migrations.RunPython(
            code=create_industries,
        ),
        migrations.AddField(
            model_name='industry',
            name='created_by',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                related_name='industry_industry_related', to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='industry',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelManagers(
            name='industry',
            managers=[
                ('objects', industry.manager.IndustryManager()),
            ],
        ),
    ]
