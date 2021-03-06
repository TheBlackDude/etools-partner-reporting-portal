# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicef', '0002_progressreport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmedocument',
            name='status',
            field=models.CharField(choices=[('Dra', 'Draft'), ('Act', 'Active'), ('Imp', 'Implemented'), ('Rej', 'Rejected')], default='Dra', max_length=256, verbose_name='PD/SSFA status'),
        ),
    ]
