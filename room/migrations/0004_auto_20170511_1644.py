# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(choices=[('DE', 'Dark Elf'), ('OR', 'Orc'), ('MG', 'Magician'), ('HU', 'Human'), ('DW', 'Dwarf'), ('W', 'Werewolf'), ('DR', 'Driada')], max_length=6),
        ),
    ]
