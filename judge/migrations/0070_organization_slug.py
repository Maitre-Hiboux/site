# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 01:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
from django.utils.text import slugify


def populate_slug(apps, schema_editor):
    Organization = apps.get_model('judge', 'Organization')
    db_alias = schema_editor.connection.alias
    for organization in Organization.objects.using(db_alias).all():
        organization.slug = slugify(organization.name)
        organization.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0069_judge_blocking'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='Organization name shown in URL', max_length=128, null=True, verbose_name='organization slug'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='key',
            field=models.CharField(help_text='Organization name shows in URL', max_length=6, null=True, unique=True, validators=[django.core.validators.RegexValidator(b'^[A-Za-z0-9]+$', b'Identifier must contain letters and numbers only')], verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=128, verbose_name='organization title'),
        ),
        migrations.RunPython(
            populate_slug,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(help_text='Organization name shown in URL', max_length=128, verbose_name='organization slug'),
        ),
    ]
