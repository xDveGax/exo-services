# Generated by Django 2.2.2 on 2019-06-05 11:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import multiselectfield.db.fields
import utils.descriptors.choices_descriptor_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0014_merge_20190528_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantSow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('C', 'Pending'), ('A', 'Accepted'), ('B', 'Declined')], default='C', max_length=1)),
                ('title', models.CharField(max_length=200)),
                ('requester_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('mode', models.CharField(choices=[('S', 'OnSite'), ('L', 'OnLine')], default='S', max_length=1)),
                ('location', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('place_id', models.CharField(blank=True, max_length=255, null=True)),
                ('location_url', models.URLField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('role', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('entity', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('budget', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('budget_currency', models.CharField(blank=True, choices=[('E', 'EUR'), ('D', 'USD')], default='D', max_length=1, null=True)),
                ('virtual_budget', models.FloatField(blank=True, default=0, null=True)),
                ('virtual_budget_currency', models.CharField(blank=True, choices=[('X', 'EXOS')], default='X', max_length=1, null=True)),
                ('extra_expenses', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(utils.descriptors.choices_descriptor_mixin.ChoicesDescriptorMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(choices=[('F', 'Draft'), ('P', 'Pending'), ('B', 'Requested'), ('J', 'Rejected'), ('T', 'Accepted'), ('D', 'Declined'), ('V', 'Removed'), ('G', 'Selected'), ('A', 'SOW Accepted'), ('C', 'SOW Declined'), ('L', 'Cancelled')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='applicantstatus',
            name='status',
            field=models.CharField(choices=[('F', 'Draft'), ('P', 'Pending'), ('B', 'Requested'), ('J', 'Rejected'), ('T', 'Accepted'), ('D', 'Declined'), ('V', 'Removed'), ('G', 'Selected'), ('A', 'SOW Accepted'), ('C', 'SOW Declined'), ('L', 'Cancelled')], default='B', max_length=1),
        ),
        migrations.CreateModel(
            name='ApplicantSOWStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', models.CharField(choices=[('C', 'Pending'), ('A', 'Accepted'), ('B', 'Declined')], default='C', max_length=1)),
                ('reasons_declined', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('incorrect', 'Incorrect data'), ('economic', 'Economic disagreement'), ('date', 'Date unavailability'), ('other', 'Other')], max_length=29, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('applicant_sow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='opportunities.ApplicantSow')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='applicantsow',
            name='applicant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opportunities.Applicant'),
        ),
    ]
