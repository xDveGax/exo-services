# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings

import model_utils.fields
import utils.mixins.location_timezone_mixin
import utils.images.fields
import utils.models.slug_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exo_accounts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('industry', '0001_squashed_0004_auto_20171016_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
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
                (
                    'slug', utils.models.slug_field.TagAutoSlugField(
                        always_update=True,
                        editable=False, null=True, populate_from='name', unique=True,
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Organization Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('annual_revenue', models.BigIntegerField(blank=True, null=True)),
                ('contact_person', models.TextField(blank=True, null=True, verbose_name='Contact Person')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin')),
                ('google', models.URLField(blank=True, null=True, verbose_name='Google +'),),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('blog', models.URLField(blank=True, null=True, verbose_name='Blog')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                (
                    'customer_type', models.CharField(
                        choices=[
                            ('N', 'Normal'), ('T', 'Training'),
                        ], default='N', max_length=1,
                    ),
                ),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='industry.Industry')),
                ('market_value', models.BigIntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postcode')),
                (
                    'profile_picture', utils.images.fields.PowerImageField(blank=True, choice_field='selectable_profile_picture', null=True, thumbnails=(
                        (32, 32), (56, 56), (150, 150), (24, 24), (48, 48), (96, 96), (144, 144)), upload_to='avatars', verbose_name='profile picture'),
                ),
                (
                    'selectable_profile_picture', models.CharField(
                        blank=True, choices=[
                            ('theme/gallery/1.jpg', 'Image1.jpg'),
                        ], default='theme/gallery/1.jpg', help_text='An image fallback when no profile picture uploaded', max_length=255, verbose_name='selected profile picture',
                    ),
                ),
                (
                    'size', models.CharField(
                        choices=[
                            ('1', 'Small: 1-10 staff'), ('2', 'Medium: 11-100 staff'),
                            ('3', 'Large: 100-500'), ('4', 'Very large: 500+'),
                        ], max_length=1, null=True,
                    ),
                ),
                ('website', models.CharField(blank=True, max_length=300, null=True, verbose_name='Website')),
                (
                    'timezone', utils.mixins.location_timezone_mixin.TimeZoneField(blank=True, null=True),
                ),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('place_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'permissions': (
                    ('edit_customer', 'Edit Customer information'),
                    ('add_user', 'Add user role'),
                    ('remove_customer', 'Remove Customer'),
                    ('view_customer', 'View General Customer information'),
                    ('list_customer', 'List customer')),
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
