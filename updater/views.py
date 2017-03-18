from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Pcap
from .forms import PcapForm
from core.models import Perfil
import core.views as core;
import json

@login_required
def index(request):
    if request.method == 'POST':

        form = PcapForm(request.POST, request.FILES)
        if form.is_valid():

            pcap = Pcap(docfile=request.FILES['docfile'])
            pcap.user = request.user
            pcap.date = timezone.now()
            pcap.save()
            core.process_pcap(pcap.pk, request.user)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('index'))
    else:
        form = PcapForm()
    return render(request, 'index.html', {'form': form})

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


