# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-08-12 09:43
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
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
            name='CertificationCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('seats', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('currency', models.CharField(choices=[('EUR', 'EURO'), ('USD', 'Dollar'), ('GBP', 'Pound Sterling')], default='EUR', max_length=4)),
                ('invoice_concept', models.CharField(max_length=255)),
                ('level', models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'Exponential Organizations'), ('level_2_ft', 'Exponential Organizations Fastrack'), ('level_3', 'Exponential Transformation')], default='level_2', max_length=20)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('O', 'Open'), ('C', 'Closed'), ('F', 'Finished')], default='D', max_length=1)),
            ],
            options={
                'verbose_name': 'Certification Cohort',
                'verbose_name_plural': 'Certification Cohorts',
            },
        ),
        migrations.CreateModel(
            name='CertificationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('payment_uuid', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_url', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Paid'), ('F', 'Completed'), ('C', 'Cancelled')], default='P', max_length=1)),
                ('price', models.FloatField()),
                ('application_details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification_requests', to='exo_certification.CertificationCohort')),
            ],
            options={
                'verbose_name': 'Certification Request',
                'verbose_name_plural': 'Certification Requests',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('level', models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'Exponential Organizations'), ('level_2_ft', 'Exponential Organizations Fastrack'), ('level_3', 'Exponential Transformation')], max_length=20)),
                ('max_uses', models.IntegerField(default=10)),
                ('uses', models.IntegerField(default=0)),
                ('discount', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='certificationrequest',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification_requests', to='exo_certification.Coupon'),
        ),
        migrations.AddField(
            model_name='certificationrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification_request', to=settings.AUTH_USER_MODEL),
        ),
    ]
