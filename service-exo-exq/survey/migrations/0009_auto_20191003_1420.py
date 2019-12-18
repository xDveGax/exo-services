# Generated by Django 2.2.6 on 2019-10-03 14:20

from django.db import migrations, models
from django.core.management import call_command
from django.conf import settings


def load_questions(apps, schema_editor):
    if settings.TEST_MODE or settings.POPULATOR_MODE:
        call_command('load_questions')
    call_command('update_questions')


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_resultlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='value_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='value_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='name_en',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='name_es',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.RunPython(load_questions)
    ]
