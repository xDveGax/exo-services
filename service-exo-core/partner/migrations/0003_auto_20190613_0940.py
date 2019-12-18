# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-13 09:40
from __future__ import unicode_literals

from django.db import migrations
import utils.images.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_auto_20181218_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='profile_picture',
            field=utils.images.fields.PowerImageField(blank=True, choice_field='selectable_profile_picture', null=True, thumbnails=((32, 32), (56, 56), (150, 150), (24, 24), (48, 48), (96, 96), (144, 144)), upload_to='avatars', verbose_name='profile picture'),
        ),
    ]
