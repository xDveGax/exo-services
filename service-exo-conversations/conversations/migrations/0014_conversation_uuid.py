# Generated by Django 2.2.1 on 2019-06-04 20:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0013_auto_20190603_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
