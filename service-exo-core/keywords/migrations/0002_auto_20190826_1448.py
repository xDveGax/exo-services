# Generated by Django 2.2.4 on 2019-08-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0001_squashed_0004_auto_20171031_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='public',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
