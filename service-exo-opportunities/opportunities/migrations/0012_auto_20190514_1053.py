# Generated by Django 2.2.1 on 2019-05-14 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_auto_20190514_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='declined_message',
            new_name='response_message',
        ),
    ]
