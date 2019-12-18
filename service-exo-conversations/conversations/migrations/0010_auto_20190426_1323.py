# Generated by Django 2.2 on 2019-04-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0009_auto_20190326_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='_type',
            field=models.CharField(choices=[('O', 'Opportunities'), ('P', 'Project')], max_length=1),
        ),
        migrations.AlterField(
            model_name='conversationuser',
            name='short_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
