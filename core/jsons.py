from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Perfil, Link, Dns, Location

from updater.models import Pcap
from updater.jsons import getRealName

from .integrations import getVendor
from .integrations import getTacytApps

import json


@login_required
def getProfiles(request):

    if 'pcap' in request.GET:
        pcap = request.GET['pcap']
        auxp = Pcap.objects.get(pk=pcap)
        perfiles = Perfil.objects.filter(pcap=auxp)
    else :
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
def getLinks(request):

    id = request.GET['perfil']
    p = get_object_or_404(Perfil, pk=id)

    links = Link.objects.filter(Q(perfil_dst=p) | Q(perfil_src=p)).order_by('time')

    array = []
    for l in  links:
        aux = {}
        aux['id'] = l.id
        aux['ipSrc'] = jsonFromIp(l.ip_src, l.pcap)
        aux['ipDst'] = jsonFromIp(l.ip_dst, l.pcap)
        aux['perfilSrc'] = l.perfil_src.mac
        aux['perfilDst'] = l.perfil_dst.mac
        aux['host'] = normalizeHost(l.host)
        aux['time'] = p.created_date.strftime("%d-%m-%Y a las %H:%M")
        array.append(aux);

    dataj = json.dumps(array)
    return HttpResponse(dataj, content_type='application/json')

@login_required
def getApps(request):

    id = request.GET['link']
    l = get_object_or_404(Link, pk=id)

    host = l.host
    host = host[2:len(host)-1]

    list = getTacytApps(host)
    array = []
    for l in  list:
        aux = {}
        aux['name'] = l.get('title')
        aux['package'] = l.get('packageName')

        array.append(aux);

    dataj = json.dumps(array)
    return HttpResponse(dataj, content_type='application/json')


def jsonFromIp(ip, pcap):
    aux= {}
    aux['ip'] = ip

    dns = Dns.objects.filter(ip=ip).first();
    if dns is None:
        dns=''
    else:
        dns = dns.host
    aux['dns'] = dns

    location = Location.objects.filter(ip=ip).filter(pcap=pcap).first();
    if location is not None:
        locationAux = {}
        locationAux['country'] = location.country
        locationAux['city'] = location.city
        locationAux['org'] = location.org
        aux['location'] = locationAux

    return aux

def normalizeHost(host):
    return host[2:len(host)-1]

@login_required
def getDetailsPerfil(request):

    id = request.GET['perfil']
    p = get_object_or_404(Perfil, pk=id)
    vendor = getVendor(id)

    aux = {}
    aux['id'] = p.mac
    aux['user'] = p.user.username
    aux['nom'] = getRealName(p.pcap.docfile.name)
    aux['fecha'] = p.created_date.strftime("%d-%m-%Y a las %H:%M")
    aux['vendor'] = vendor.fabricante
    aux['os'] = p.os
    aux['tlf'] = p.telefono
    data = json.dumps(aux)

    return HttpResponse(data, content_type='application/json')

@login_required
def getUserAgents(request):

    id = request.GET['perfil']
    p = get_object_or_404(Perfil, pk=id)

    user_agents = Link.objects.filter(perfil_src=p).exclude(user_agent='').values('user_agent').distinct()

    lista = []
    for u in  user_agents:
        lista.append(u)

    data = json.dumps(lista)
    return HttpResponse(data, content_type='application/json')






















