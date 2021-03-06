# Generated by Django 2.1.7 on 2019-02-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20190124_0740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterModelOptions(
            name='messagelog',
            options={'verbose_name': 'MessageLog', 'verbose_name_plural': 'MessageLogs'},
        ),
        migrations.AddField(
            model_name='message',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_email',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
