# Generated by Django 2.2.6 on 2019-10-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_auto_20191003_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('es', 'Spanish')], default='en', max_length=2, null=True),
        ),
    ]
