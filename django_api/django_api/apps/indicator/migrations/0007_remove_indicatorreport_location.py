# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0006_auto_20170528_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicatorreport',
            name='location',
        ),
    ]
