# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='date_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]