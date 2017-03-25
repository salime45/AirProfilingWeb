# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Perfil
from .models import Link
from .models import Location

from updater.forms import PcapForm

from .integrations import getLocation

import datetime;

from scapy.all import *
import scapy_http.http as scapyh


@login_required
def index(request):
    return render(request, 'index.html', {'form': PcapForm()})

@login_required
def getPerfilDetails(request):
    id = request.GET['id']
    perfil = get_object_or_404(Perfil, pk=id)
    return render(request, 'perfil.html', {'perfil': perfil})


#Función que procesa un pcap para optener perfiles y sus links asociados.
def process_pcap(pcap, user):

    #path = "/home/imonje/air_profiling" + pcap.docfile.url
    path = pcap.docfile.path
    print(path)

    packets = rdpcap(path)
    for i in range(len(packets)):

        p = packets[i]
        'Obtenemos los perfiles asociados'
        perfil_src = getPerfil(p.src, pcap)
        perfil_dst = getPerfil(p.dst, pcap)

        'Generamos los links'
        getLink(p, perfil_src, perfil_dst, pcap)

#Funcion que obtiene un perfil de la BD o lo crea si no existe
def getPerfil(mac, pcap):

    try:
        perfil =  Perfil.objects.get(mac=mac)
    except Perfil.DoesNotExist:
        perfil = None

    if perfil is None:
        perfil = Perfil()
        perfil.mac = mac
        perfil.user = pcap.user
        perfil.pcap = pcap
        perfil.save()

    return perfil

#Función que procesa un paquete para un link.
def getLink(packet, perfil_src, perfil_dst, pcap):

    # si el paquete tiene capa ip lo procesamos
    if IP in packet:
        l =  Link();
        l.pcap = pcap
        l.perfil_src = perfil_src
        l.perfil_dst = perfil_dst
        l.ip_dst = packet[IP].dst
        l.ip_src = packet[IP].src
        l.time = getDate(packet.time)

        #si es un paquete HTTP
        if scapyh.HTTPRequest in packet:
            l.user_agent = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "User-Agent"))
            l.host = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "Host"))

        l.save()

        #Comprobamos si la ip tiene un objeto location asociado, si no es asi generamos uno
        location_src = Location.objects.filter(ip=l.ip_src).filter(pcap=l.pcap).first()
        location_dst = Location.objects.filter(ip=l.ip_dst).filter(pcap=l.pcap).first()

        if location_src is None:
           getLocation(l.ip_src, l.pcap)
        if location_dst is None:
           getLocation(l.ip_dst, l.pcap)


def getFormatDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')

def getDate(time):
    return datetime.datetime.fromtimestamp(time)














