# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-04 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exo_accounts', '0002_auto_20190710_0710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('user_edit_profile', 'Edit User Profile'), ('view_marketplace_full', 'Can view Marketplace')), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
