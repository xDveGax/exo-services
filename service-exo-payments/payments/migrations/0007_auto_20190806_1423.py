# Generated by Django 2.2.4 on 2019-08-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_auto_20190806_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceSerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=5)),
                ('current', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='amount_vat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='vat',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
