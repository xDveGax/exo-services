# Generated by Django 2.2.4 on 2019-08-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_payment_send_by_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='generate_and_send_invoice',
            field=models.BooleanField(default=False),
        ),
    ]
