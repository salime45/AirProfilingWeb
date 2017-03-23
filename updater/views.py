# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Pcap
from core.views import process_pcap
from .forms import PcapForm

import _thread

@login_required
def updatePcap(request):
    if request.method == 'POST':

        form = PcapForm(request.POST, request.FILES)
        if form.is_valid():

            pcap = Pcap(docfile=request.FILES['docfile'])
            pcap.user = request.user
            pcap.date = timezone.now()

            #Comprobamos el tamaño y la extensión del fichero
            if pcap.docfile.size > 104857600:
                 return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo es demasiado grande.'})

            print("--->" +  pcap.docfile.name)

            if not pcap.docfile.name.endswith(".pcap") and not pcap.docfile.name.endswith(".pcapng"):
                 return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo no es valido.'})

            pcap.save()
            #creamos un thread para no hacer esperar al usuario
            _thread.start_new_thread( process_pcap, (pcap.pk, request.user) )
            #process_pcap(pcap.pk, request.user)

            # Redirect to the document list after POST
            return render(request, 'index.html', {'form': PcapForm(), 'msg': 'El archivo se ha subido correctamente y se esta procesando. La información puede tardar un tiempo en estar completa.'})


@login_required
def getPcap(request):
    id = request.GET['pcap']
    pcap = get_object_or_404(Pcap, pk=id)
    return render(request, 'pcap.html', {'pcap': pcap})





