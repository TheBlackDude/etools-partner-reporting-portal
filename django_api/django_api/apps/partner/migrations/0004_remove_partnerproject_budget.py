# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0003_partner_type_of_assessment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerproject',
            name='budget',
        ),
    ]
