# Generated by Django 2.2.5 on 2019-10-04 18:28

from django.db import migrations, models
import uuid


def populate_cohort_uuid(apps, schema_editor):
    CertificationCohort = apps.get_model(
        'exo_certification',
        'certificationcohort',
    )

    for cohort in CertificationCohort.objects.all():
        cohort.uuid = uuid.uuid4()
        cohort.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('exo_certification', '0012_auto_20191002_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationcohort',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(populate_cohort_uuid),
        migrations.AlterField(
            model_name='certificationcohort',
            name='uuid',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),

    ]
