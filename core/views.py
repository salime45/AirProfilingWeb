from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Perfil
from .models import Link
from updater.models import Pcap

from updater.forms import PcapForm

from .integrations import getLocation

import datetime;

from scapy.all import *
import scapy_http.http as scapyh


@login_required
def index(request):
    return render(request, 'index.html', {'form': PcapForm()})


def getFormatDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')

def getDate(time):
    return datetime.datetime.fromtimestamp(time)


def process_pcap(pk_pcap, user):

    'abrimos el pcap y lo recorremos'
    pcap = Pcap.objects.get(pk=pk_pcap)

    #path = "/home/imonje/air_profiling" + pcap.docfile.url
    path = pcap.docfile.path
    print(path)

    packets = rdpcap(path)
    for i in range(len(packets)):

        p = packets[i]

        try:
            perfil =  Perfil.objects.get(mac=p.src)
        except Perfil .DoesNotExist:
            perfil = None

        if perfil is None:
            print("nuevo...")
            perfil = Perfil()
            perfil.mac = p.src
            perfil.user = user
            perfil.pcap = pcap
            perfil.save()

        #print("mac : " + str(p.src))
        getLink(p, perfil, pcap)

    return True


def getLink(packet, perfil, pcap):

    l =  Link();
    l.pcap = pcap
    l.perfil = perfil
    l.time = getDate(packet.time)

    if IP in packet:
        l.ip = packet[IP].dst
        link = Link.objects.filter(ip=l.ip).filter(pcap=l.pcap).first()
        if link is None:
           l.geoposition = getLocation(l.ip)
        else:
            l.geoposition = link.geoposition

    if scapyh.HTTPRequest in packet:
        l.user_agent = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "User-Agent"))
        l.host = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "Host"))
        l.cabezera = packet[scapyh.HTTPRequest].show();
        print(packet[scapyh.HTTPRequest].show())

    l.save()

















