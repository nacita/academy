# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 14:09
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='channeled_location',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=255, null=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='survey',
            name='channeled_location_other',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=255, null=True), default=list, size=None),
        ),
    ]
