# Generated by Django 2.2.2 on 2019-06-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_url_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='alternative_payment_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='alternative_payment_mode',
            field=models.CharField(blank=True, choices=[('T', 'Tokens'), ('B', 'Bank transfer')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='concept',
            field=models.CharField(max_length=512),
        ),
    ]
