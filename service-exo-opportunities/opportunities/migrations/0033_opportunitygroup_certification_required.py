# Generated by Django 2.2.7 on 2019-11-08 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exo_role', '0001_initial'),
        ('opportunities', '0032_auto_20191108_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunitygroup',
            name='certification_required',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='exo_role.CertificationRole'),
        ),
    ]
