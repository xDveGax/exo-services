# Generated by Django 2.2.6 on 2019-10-21 13:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exo_certification', '0013_certificationcohort_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificationcohort',
            name='level',
        ),
        migrations.RemoveField(
            model_name='certificationrequest',
            name='level',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='level',
        ),
        migrations.AlterField(
            model_name='certificationcohort',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
