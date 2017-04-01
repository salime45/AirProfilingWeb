from __future__ import unicode_literals
from django.utils import timezone

from django.db import models



class Link(models.Model):
    perfil_src = models.ForeignKey('core.Perfil',  related_name='perfil_src')
    ip_src = models.CharField(max_length=50)
    perfil_dst = models.ForeignKey('core.Perfil',  related_name='perfil_dst')
    ip_dst = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=200)
    pcap = models.ForeignKey('updater.Pcap')
    time = models.DateTimeField()

class Location (models.Model):
    ip = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    pcap = models.ForeignKey('updater.Pcap')
    timezone = models.CharField(max_length=150)
    countryCode = models.CharField(max_length=50)
    org = models.CharField(max_length=250)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=250)
    regionName = models.CharField(max_length=250)
    isp = models.CharField(max_length=250)
    city = models.CharField(max_length=150)

class Perfil(models.Model):
    mac = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    dispositivo = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User')
    pcap = models.ForeignKey('updater.Pcap')
    created_date = models.DateTimeField(default=timezone.now)

class Vendor(models.Model):
    mac = models.CharField(max_length=10, primary_key=True)
    fabricante = models.CharField(max_length=200)

class Dns(models.Model):
    ip = models.CharField(max_length=50, primary_key=True)
    host = models.CharField(max_length=200)

class UserAgent(models.Model):
    value = models.CharField(max_length=200, primary_key=True)
    os = models.CharField(max_length=200)
    browser = models.CharField(max_length=200)
    device = models.CharField(max_length=200)



