# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-07 11:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_teamstep'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0012_auto_20180613_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermicrolearning',
            options={'verbose_name': 'User MicroLearning', 'verbose_name_plural': 'User Microlearnings'},
        ),
        migrations.AlterUniqueTogether(
            name='usermicrolearning',
            unique_together=set([('user', 'microlearning', 'team')]),
        ),
    ]
