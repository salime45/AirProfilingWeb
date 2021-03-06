# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-25 10:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('updater', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_src', models.CharField(max_length=50)),
                ('ip_dst', models.CharField(max_length=50)),
                ('host', models.CharField(max_length=50)),
                ('user_agent', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('pcap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updater.Pcap')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=150)),
                ('countryCode', models.CharField(max_length=50)),
                ('org', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=250)),
                ('regionName', models.CharField(max_length=250)),
                ('isp', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=150)),
                ('pcap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updater.Pcap')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('mac', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('dispositivo', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pcap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updater.Pcap')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='perfil_dst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_dst', to='core.Perfil'),
        ),
        migrations.AddField(
            model_name='link',
            name='perfil_src',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_src', to='core.Perfil'),
        ),
    ]
