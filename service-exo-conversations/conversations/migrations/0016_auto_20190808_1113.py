# Generated by Django 2.2.3 on 2019-08-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0015_auto_20190808_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationuser',
            name='profile_url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
