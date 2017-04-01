from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

def generate_filename(self, filename):
    url = "pcaps/%s/%s" % (self.user.username, filename)
    return url

class Pcap(models.Model):
    user = models.ForeignKey('auth.User')
    docfile = models.FileField(upload_to=generate_filename)
    date = models.DateTimeField(default=timezone.now)
    procesado = models.BooleanField()