# Generated by Django 2.2.8 on 2019-12-10 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exo_role', '0001_initial'),
        ('event', '0011_auto_20191128_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='exo_role.Category'),
        ),
        migrations.AddField(
            model_name='participant',
            name='exo_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_participants', to='exo_role.ExORole'),
        ),
        migrations.AlterField(
            model_name='event',
            name='type_event',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='participant',
            name='role',
            field=models.CharField(max_length=3),
        ),
    ]
