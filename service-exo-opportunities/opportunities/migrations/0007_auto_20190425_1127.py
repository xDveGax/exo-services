# Generated by Django 2.2 on 2019-04-25 11:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0006_auto_20181213_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='virtual_budget',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='virtual_budget_currency',
            field=models.CharField(blank=True, choices=[('X', 'EXOS')], default='X', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='budget_currency',
            field=models.CharField(blank=True, choices=[('E', 'EUR'), ('D', 'USD')], default='D', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
