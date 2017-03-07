from django.shortcuts import render
from .models import Perfil, Link
from updater.models import Pcap

import datetime;

from scapy.all import *


def getDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')

def process_pcap(pk_pcap, user):

    'abrimos el pcap y lo recorremos'
    pcap = Pcap.objects.get(pk=pk_pcap)

    path = "/home/imonje/air_profiling" + pcap.docfile.url
    print(path)

    packets = rdpcap(path)
    for i in range(len(packets)):
        print("indice : " + str(i))

        p = packets[i]
        print("mac : " + str(p.src))

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


    return True