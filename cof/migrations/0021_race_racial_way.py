# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0020_racialway'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='racial_way',
            field=models.ManyToManyField(to='cof.RacialWay'),
        ),
    ]
