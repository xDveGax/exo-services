# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-04 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exo_certification', '0010_merge_20190902_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationcohort',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('ES', 'Spanish')], default='EN', max_length=3),
        ),
        migrations.AlterField(
            model_name='certificationcohort',
            name='level',
            field=models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'ExO Consultant'), ('level_2_ft', 'ExO Consultant Fastrack'), ('level_3', 'ExO Sprint Coach')], default='level_2', max_length=20),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='level',
            field=models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'ExO Consultant'), ('level_2_ft', 'ExO Consultant Fastrack'), ('level_3', 'ExO Sprint Coach')], default='level_2', max_length=10),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='level',
            field=models.CharField(choices=[('level_1', 'ExO Foundations'), ('level_2', 'ExO Consultant'), ('level_2_ft', 'ExO Consultant Fastrack'), ('level_3', 'ExO Sprint Coach')], max_length=20),
        ),
    ]
