# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0010_auto_20170620_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorblueprint',
            name='calculation_formula',
            field=models.CharField(choices=[('sum', 'sum'), ('max', 'max'), ('avg', 'avg'), ('min', 'min')], default='sum', max_length=3),
        ),
        migrations.AlterField(
            model_name='indicatorblueprint',
            name='unit',
            field=models.CharField(choices=[('number', 'number'), ('percentage', 'percentage'), ('likert', 'likert'), ('yesno', 'yesno')], default='number', max_length=10),
        ),
    ]
