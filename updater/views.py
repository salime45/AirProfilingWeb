from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Pcap
from core.views import getProfiles

import json


@login_required
def getPcaps(request):
    pcaps = Pcap.objects.all()
    array = []
    for p in  pcaps:
        aux = {}
        aux['id'] = p.id
        aux['user'] = p.user.username
        aux['nom'] = getRealName(p.docfile.name)
        aux['fecha'] = p.date.strftime("%d-%m-%Y a las %H:%M")
        array.append(aux);

    dataj = json.dumps(array)
    return HttpResponse(dataj, content_type='application/json')


@login_required
def getPcap(request):
    id = request.GET['pcap']
    pcap = get_object_or_404(Pcap, pk=id)
    return render(request, 'pcap.html', {'pcap': pcap})

@login_required
def getDetailsPcap(request):

    id = request.GET['pcap']
    p = get_object_or_404(Pcap, pk=id)
    aux = {}
    aux['id'] = p.id
    aux['user'] = p.user.username
    aux['nom'] = getRealName(p.docfile.name)
    aux['fecha'] = p.date.strftime("%d-%m-%Y a las %H:%M")
    data = json.dumps(aux)

    return HttpResponse(data, content_type='application/json')


def getRealName(name):
    folders = name.split("/")
    return folders[len( folders ) - 1]



