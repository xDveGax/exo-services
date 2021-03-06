# Generated by Django 2.1.7 on 2019-03-28 17:08

import django_extensions.db.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import event.managers.event
import event.managers.participant
import model_utils.fields
import multiselectfield.db.fields
import utils.descriptors.choices_descriptor_mixin
import utils.mixins.location_timezone_mixin
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('created_by_full_name', models.CharField(max_length=255)),
                ('timezone', utils.mixins.location_timezone_mixin.TimeZoneField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('place_id', models.CharField(blank=True, max_length=255, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('_status', models.CharField(choices=[('P', 'Pending'),
                                                      ('H', 'Public'), ('D', 'Deleted')], default='H', max_length=1)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('type_event', models.CharField(choices=[
                 ('T', 'ExO Talk'), ('B', 'ExO Book launch'), ('W', 'ExO Workshop'), ('S', 'ExO Summit')], default='W', max_length=1)),
                ('follow_type', multiselectfield.db.fields.MultiSelectField(choices=[
                 ('P', 'On Site'), ('S', 'Streaming'), ('O', 'Online')], default='P', max_length=5)),
                ('url', models.CharField(blank=True, max_length=512, null=True)),
                ('languages', django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(max_length=56), size=None)),
                ('show_price', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0, null=True)),
                ('currency', models.CharField(choices=[('E', '€'), ('D', '$')], default='E', max_length=1)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='event_event_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-start'],
                'permissions': (('edit-event', 'Edit Event'), ('delete-event', 'Delete Event')),
            },
            bases=(utils.descriptors.choices_descriptor_mixin.ChoicesDescriptorMixin, models.Model),
            managers=[
                ('objects', event.managers.event.AllEventManager()),
                ('public_objects', event.managers.event.EventManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('created_by_full_name', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(blank=True, editable=False, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Organizer Email')),
                ('url', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='event_organizer_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('created_by_full_name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255, verbose_name='User name')),
                ('user_email', models.EmailField(max_length=255, verbose_name='User email')),
                ('order', models.IntegerField(default=0)),
                ('role', models.CharField(choices=[('P', 'Participant'),
                                                   ('O', 'Organizer'), ('S', 'Speaker')], default='P', max_length=1)),
                ('status', models.CharField(choices=[('A', 'Active'),
                                                     ('D', 'Deleted'), ('P', 'Pending')], default='A', max_length=1)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='event_participant_related', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='participants', to='event.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
            bases=(utils.descriptors.choices_descriptor_mixin.ChoicesDescriptorMixin, models.Model),
            managers=[
                ('objects', event.managers.participant.ParticipantManager()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(blank=True, related_name='events', to='event.Organizer'),
        ),
    ]
