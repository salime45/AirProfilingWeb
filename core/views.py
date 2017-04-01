# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Perfil

from updater.forms import PcapForm


@login_required
def index(request):
    return render(request, 'index.html', {'form': PcapForm()})

@login_required
def getPerfil(request):
    id = request.GET['id']
    perfil = get_object_or_404(Perfil, pk=id)
    return render(request, 'perfil.html', {'perfil': perfil})
















