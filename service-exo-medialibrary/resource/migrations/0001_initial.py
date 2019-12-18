# Generated by Django 2.1.3 on 2018-11-23 10:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
import multiselectfield.db.fields
import resource.managers.category
import resource.managers.resource
import resource.managers.tag
import resource.models.mixins.video_resource_mixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True)),
                ('extra_data', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('objects', resource.managers.category.CategoryManager()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('V', 'Video Vimeo'), ('Y', 'Video Youtube'), ('D', 'Video Drive'), ('X', 'Video Dropbox'), ('F', 'Filestack')], default='V', max_length=1)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('A', 'Available'), ('E', 'Error'), ('R', 'Removed')], default='D', max_length=1)),
                ('name', models.CharField(max_length=555)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('sections', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'Sprint'), ('A', 'Sprint Automated'), ('W', 'Workshop'), ('F', 'Fastrack'), ('E', 'Ecosystem'), ('P', 'Speakers'), ('T', 'Trainers'), ('C', 'Consultants'), ('O', 'Coaches'), ('L', 'Alumni'), ('D', 'Delivery and partner')], max_length=21, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('extra_data', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(resource.models.mixins.video_resource_mixin.VideoResourceMixin, models.Model),
            managers=[
                ('objects', resource.managers.resource.ResourceManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True)),
                ('default_show_filter', models.BooleanField(default=False)),
                ('extra_data', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='resource.Category')),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('objects', resource.managers.tag.TagManager()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(blank=True, to='resource.Tag'),
        ),
    ]
