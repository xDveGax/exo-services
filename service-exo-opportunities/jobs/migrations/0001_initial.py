# Generated by Django 2.2.6 on 2019-10-27 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opportunities', '0030_auto_20191112_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('applicant', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='job', to='opportunities.Applicant')),
            ],
        ),
    ]
