# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dns',
            fields=[
                ('ip', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('value', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=200)),
                ('browser', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
            ],
        ),
    ]
