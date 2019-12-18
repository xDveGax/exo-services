# Generated by Django 2.2.5 on 2019-10-02 14:47

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0069_auto_20190826_1448'),
        ('exo_certification', '0011_auto_20190904_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificationcohort',
            name='title',
        ),
        migrations.AddField(
            model_name='certificationcohort',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='certification_cohort', to='project.Project'),
        ),
        migrations.AlterField(
            model_name='certificationcohort',
            name='level',
            field=models.CharField(choices=[('level_1', 'L1'), ('level_2', 'L2'),
                                            ('level_2_ft', 'L2A'), ('level_3', 'L3')], default='level_2', max_length=20),
        ),
        migrations.AlterField(
            model_name='certificationrequest',
            name='level',
            field=models.CharField(choices=[('level_1', 'L1'), ('level_2', 'L2'),
                                            ('level_2_ft', 'L2A'), ('level_3', 'L3')], default='level_2', max_length=10),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='level',
            field=models.CharField(choices=[('level_1', 'L1'), ('level_2', 'L2'),
                                            ('level_2_ft', 'L2A'), ('level_3', 'L3')], max_length=20),
        ),
        migrations.CreateModel(
            name='ExOCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.CharField(choices=[('L1', 'ExO Foundations'), ('L2', 'ExO Consultant'), (
                    'L2A', 'ExO Consultant Fastrack'), ('L3', 'ExO Sprint Coach')], db_index=True, default='L2', max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'ExO Certification',
                'verbose_name_plural': 'ExO Certifications',
            },
        ),
        migrations.AddField(
            model_name='certificationcohort',
            name='certification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='cohorts', to='exo_certification.ExOCertification'),
        ),
        migrations.AddField(
            model_name='certificationrequest',
            name='certification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='certification_requests', to='exo_certification.ExOCertification'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='certification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='coupons', to='exo_certification.ExOCertification'),
        ),
    ]
