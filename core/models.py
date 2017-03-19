from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Perfil(models.Model):
    mac = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    dispositivo = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User')
    pcap = models.ForeignKey('updater.Pcap')
    created_date = models.DateTimeField(default=timezone.now)


class Link(models.Model):
    perfil = models.ForeignKey('core.Perfil')
    pcap = models.ForeignKey('updater.Pcap')
    ip = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    geoposition = models.CharField(max_length=50)
    user_agent = models.CharField(max_length=200)
    cabecera = models.TextField()
    time = models.DateTimeField()