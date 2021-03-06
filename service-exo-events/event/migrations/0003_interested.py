# Generated by Django 2.2.4 on 2019-08-22 07:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20190607_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('event', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='interested', to='event.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
