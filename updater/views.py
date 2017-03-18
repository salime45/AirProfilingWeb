from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Pcap

import json


@login_required
def getPcaps(request):
    pcaps = Pcap.objects.all()
    array = []
    for p in  pcaps:
        aux = {}
        aux['user'] = p.user.username
        aux['nom'] = p.docfile.url
        aux['fecha'] = p.date.strftime("%d-%m-%Y a las %H:%M")
        array.append(aux);

    dataj = json.dumps(array)
    return HttpResponse(dataj, content_type='application/json')



