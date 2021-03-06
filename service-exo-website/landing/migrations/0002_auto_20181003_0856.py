# Generated by Django 2.1.1 on 2018-10-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='theme',
            field=models.CharField(choices=[('forty', 'Forty'), ('stellar', 'Stellar')], default='forty', max_length=100),
        ),
    ]
