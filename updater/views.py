# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Pcap
from .forms import PcapForm

@login_required
def updatePcap(request):
    if request.method == 'POST':

        form = PcapForm(request.POST, request.FILES)
        if form.is_valid():

            pcap = Pcap(docfile=request.FILES['docfile'])
            pcap.user = request.user
            pcap.date = timezone.now()
            pcap.procesado = False

            #Comprobamos el tamaño y la extensión del fichero
            if pcap.docfile.size > 104857600:
                 return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo es demasiado grande.'})

            if not pcap.docfile.name.endswith(".pcap") and not pcap.docfile.name.endswith(".pcapng"):
                 return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo no es valido.'})

            pcap.save()
            return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo se ha subido correctamente y se esta procesando. La información puede tardar un tiempo en estar completa.'})

@login_required
def getPcap(request):
    id = request.GET['pcap']
    pcap = get_object_or_404(Pcap, pk=id)
    return render(request, 'pcap.html', {'pcap': pcap})





