# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20170328_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[('DE', 'Dark Elf'), ('OR', 'Orc'), ('MG', 'Magician'), ('HU', 'Human'), ('DW', 'Dwarf'), ('V', 'Verwolf')], max_length=6)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room')),
            ],
        ),
    ]
