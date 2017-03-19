from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Perfil
from .models import Link
from updater.models import Pcap
from updater.forms import PcapForm

import datetime;
import json
import _thread

from scapy.all import *
import scapy_http.http as scapyh

@login_required
def getProfiles(request):
    perfiles = Perfil.objects.all()
    array = []
    for p in  perfiles:
        aux = {}
        aux['mac'] = p.mac
        aux['nom'] = p.name
        aux['user'] = p.user.username
        aux['fecha'] = p.created_date.strftime("%d-%m-%Y a las %H:%M")
        array.append(aux);

    dataj = json.dumps(array)
    return HttpResponse(dataj, content_type='application/json')

@login_required
def index(request):
    return render(request, 'index.html', {'form': PcapForm()})

@login_required
def updatePcap(request):
    if request.method == 'POST':

        form = PcapForm(request.POST, request.FILES)
        if form.is_valid():

            pcap = Pcap(docfile=request.FILES['docfile'])
            pcap.user = request.user
            pcap.date = timezone.now()
            pcap.save()
            _thread.start_new_thread( process_pcap, (pcap.pk, request.user) )
            #process_pcap(pcap.pk, request.user)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('index'))

def getFormatDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')

def getDate(time):
    return datetime.datetime.fromtimestamp(time)


def process_pcap(pk_pcap, user):

    'abrimos el pcap y lo recorremos'
    pcap = Pcap.objects.get(pk=pk_pcap)

    path = "/home/imonje/air_profiling" + pcap.docfile.url
    print(path)

    packets = rdpcap(path)
    for i in range(len(packets)):
        #print("indice : " + str(i))

        p = packets[i]
        #print("mac : " + str(p.src))

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

    if scapyh.HTTPRequest in packet:
        l.user_agent = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "User-Agent"))
        l.host = str(scapyh._get_field_value(packet[scapyh.HTTPRequest], "Host"))
        l.cabezera = packet[scapyh.HTTPRequest].show();
        print(packet[scapyh.HTTPRequest].show())

    l.save()

















