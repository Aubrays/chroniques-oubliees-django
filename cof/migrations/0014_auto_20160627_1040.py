# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0013_auto_20160627_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='profile1', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='slug',
            field=models.SlugField(default='race1', max_length=30, unique=True),
        ),
    ]