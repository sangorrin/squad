# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-30 13:17
from __future__ import unicode_literals

from django.db import migrations


def create_missing_project_status(apps, schema_editor):
    ProjectStatus = apps.get_model('core', 'ProjectStatus')
    Build = apps.get_model('core', 'Build')
    for build in Build.objects.all():
        ProjectStatus.objects.get_or_create(build=build)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0102_projectstatus_null_metric_summary'),
    ]

    operations = [
        migrations.RunPython(
            create_missing_project_status,
            reverse_code=migrations.RunPython.noop,
        ),
    ]