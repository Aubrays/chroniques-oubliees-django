# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0015_auto_20160627_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profiles'),
        ),
    ]
