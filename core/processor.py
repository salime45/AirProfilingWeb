# -*- coding: utf-8 -*-
from django.utils import timezone

from .models import Link
from .models import Location
from .models import Perfil
from updater.models import Pcap

from .integrations import getLocation
from .integrations import getVendor
from .integrations import getUA

from scapy.all import *
import scapy_http.http as scapyh

import datetime;

#Funcion que procesa los pcaps no procesados
def processPcaps():

    pcaps = Pcap.objects.filter(procesado=False)

    for i in range(len(pcaps)):
        pcap = pcaps[i]
        processPcap(pcap)
        pcap.procesado = True
        pcap.save()

    return len(pcaps)

#Función que procesa un pcap para optener perfiles y sus links asociados.
def processPcap(pcap):

    #path = "/home/imonje/air_profiling" + pcap.docfile.url
    path = pcap.docfile.path
    print(path)

    packets = rdpcap(path)
    print("-------> " + str(len(packets)))

    for i in range(len(packets)):

        p = packets[i]

        print("....... > " + str(i) + " /" + p.src)
        print("....... > " + str(i) + " /" + p.dst)
        'Comprobamos si son MAC validas'
        if isValidMac(p.src) and isValidMac(p.dst):

            'Generamos los links'
            processLink(p, pcap)


#Funcion que obtiene un perfil de la BD o lo crea si no existe
def processPerfil(mac, pcap):

    try:
        perfil = Perfil.objects.get(mac=mac)
    except Perfil.DoesNotExist:
        perfil = None

    if perfil is None:
        perfil = Perfil()
        perfil.mac = mac
        perfil.user = pcap.user
        perfil.pcap = pcap
        perfil.save()
        getVendor(mac)


    return perfil

#Función que procesa un paquete para un link.
def processLink(packet, pcap):


    # si el paquete tiene capa ip lo procesamos
    if IP in packet:

        'Obtenemos los perfiles asociados'
        perfil_src = processPerfil(packet.src, pcap)
        perfil_dst = processPerfil(packet.dst, pcap)

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
            #Parseamos el user agent
            getUA(l.user_agent)
        l.save()

        #Comprobamos si la ip tiene un objeto location asociado, si no es asi generamos uno
        location_src = Location.objects.filter(ip=l.ip_src).filter(pcap=l.pcap).first()
        location_dst = Location.objects.filter(ip=l.ip_dst).filter(pcap=l.pcap).first()

        if location_src is None:
           getLocation(l.ip_src, l.pcap)
        if location_dst is None:
           getLocation(l.ip_dst, l.pcap)

def isValidMac(mac):
    return mac != "ff:ff:ff:ff:ff:ff" and not mac.startswith("01")

def getFormatDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')

def getDate(time):
    time = datetime.datetime.fromtimestamp(time)
    time = timezone.make_aware(time, timezone.get_current_timezone())
    return time








