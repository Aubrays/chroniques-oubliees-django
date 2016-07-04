# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cof', '0002_auto_20160624_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicWay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way_name', models.CharField(max_length=50)),
                ('way_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_name', models.CharField(max_length=50)),
                ('rank_description', models.TextField()),
                ('rank_level', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='basicway',
            name='ranks',
            field=models.ManyToManyField(to='cof.Rank'),
        ),
    ]