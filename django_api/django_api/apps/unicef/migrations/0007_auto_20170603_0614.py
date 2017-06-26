# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-03 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicef', '0006_progressreport_programme_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressreport',
            name='challenges_in_the_reporting_period',
            field=models.CharField(max_length=256, verbose_name='Challenges/bottlenecs in the reporting period (latest)'),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='funds_received_to_date',
            field=models.CharField(max_length=256, verbose_name='Funds Received to date'),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='partner_contribution_to_date',
            field=models.CharField(max_length=256, verbose_name='Partner Contribution to date'),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='proposed_way_forward',
            field=models.CharField(max_length=256, verbose_name='Proposed way forward (latest)'),
        ),
    ]