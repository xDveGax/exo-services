# Generated by Django 2.2.7 on 2019-11-29 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_auto_20191030_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, null=True)),
                ('user_project_role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='project.UserProjectRole')),
            ],
        ),
    ]
