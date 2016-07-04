# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0023_profile_basic_ways'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommanded_traits',
            field=models.CharField(default='no-recommandation', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sup_dexterity',
            field=models.BooleanField(default=False),
        ),
    ]
