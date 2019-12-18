# Generated by Django 2.2.6 on 2019-10-22 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='project.Project'),
            preserve_default=False,
        ),
    ]
