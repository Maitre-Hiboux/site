# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0065_blogpost_perms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='submission time'),
        ),
    ]