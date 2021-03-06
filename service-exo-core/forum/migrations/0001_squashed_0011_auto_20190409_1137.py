# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-07-09 06:11
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import forum.managers.answer
import forum.managers.post
import model_utils.fields
import utils.descriptors.choices_descriptor_mixin
import utils.models.slug_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('keywords', '0001_squashed_0004_auto_20171031_1102'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('comment', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='forum_answer_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('_type', models.CharField(choices=[('C', 'Circle'), ('Q', 'Q&A Session'), ('P',
                                                                                            'Project'), ('A', 'Announcement'), ('T', 'Assignment')], default='C', max_length=1)),
                ('content_type', models.ForeignKey(null=True,
                                                   on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='forum_post_related', to=settings.AUTH_USER_MODEL)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True,
                                                       editable=False, null=True, populate_from='title', unique=True)),
                ('tags', models.ManyToManyField(to='keywords.Keyword')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-modified'],
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='answers', to='forum.Post'),
            preserve_default=False,
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objects', forum.managers.post.PostManager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='_type',
            field=models.CharField(choices=[('C', 'Circle'), ('Q', 'Q-A Session'),
                                            ('P', 'Project'), ('A', 'Announcement'), ('T', 'Assignment')], max_length=1),
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': [
                '-modified'], 'permissions': (('edit_answer', 'Edit Answer'),), 'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': [
                '-modified'], 'permissions': (('edit_post', 'Edit Post'),), 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelManagers(
            name='answer',
            managers=[
                ('objects', forum.managers.answer.AnswerManager()),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='replies', to='forum.Answer'),
        ),
        migrations.AlterField(
            model_name='post',
            name='_type',
            field=models.CharField(choices=[('C', 'Circle'), ('Q', 'Q-A Session'),
                                            ('P', 'Project'), ('A', 'Announcement'), ('T', 'Team Step')], max_length=1),
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published'),
                                            ('R', 'Removed'), ('B', 'Blocked')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published'),
                                            ('R', 'Removed'), ('B', 'Blocked')], default='P', max_length=1),
        ),
        migrations.CreateModel(
            name='PostAnswerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Published'),
                                                     ('R', 'Removed'), ('B', 'Blocked')], default='P', max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('content_type', models.ForeignKey(null=True,
                                                   on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(utils.descriptors.choices_descriptor_mixin.ChoicesDescriptorMixin, models.Model),
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objects', forum.managers.post.PostManager()),
                ('all_objects', forum.managers.post.AllPostManager()),
                ('slug_manager', forum.managers.post.AllPostManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='answer',
            managers=[
                ('objects', forum.managers.answer.AnswerManager()),
                ('all_objects', forum.managers.answer.AllAnswerManager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=utils.models.slug_field.AutoSlugCustomManagerField(
                editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
