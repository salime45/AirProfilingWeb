from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Perfil
from updater.models import Pcap
from updater.jsons import getRealName

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
def getDetailsPerfil(request):

    id = request.GET['perfil']
    p = get_object_or_404(Perfil, pk=id)
    aux = {}
    aux['id'] = p.mac
    aux['user'] = p.user.username
    aux['nom'] = getRealName(p.pcap.docfile.name)
    aux['fecha'] = p.created_date.strftime("%d-%m-%Y a las %H:%M")
    aux['dispositivo'] = ''
    aux['os'] = ''
    aux['tlf'] = p.telefono
    data = json.dumps(aux)

    return HttpResponse(data, content_type='application/json')