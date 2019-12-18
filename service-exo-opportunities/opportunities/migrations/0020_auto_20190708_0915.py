# Generated by Django 2.2.2 on 2019-07-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0019_auto_20190617_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('F', 'Draft'), ('P', 'Pending'), ('B', 'Requested'), ('J', 'Rejected'), (
                'T', 'Accepted'), ('D', 'Declined'), ('V', 'Removed'), ('G', 'Selected'), ('L', 'Cancelled')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='applicantstatus',
            name='status',
            field=models.CharField(choices=[('F', 'Draft'), ('P', 'Pending'), ('B', 'Requested'), ('J', 'Rejected'), (
                'T', 'Accepted'), ('D', 'Declined'), ('V', 'Removed'), ('G', 'Selected'), ('L', 'Cancelled')], default='B', max_length=1),
        ),
    ]
