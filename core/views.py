# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Perfil
from .models import Link

from updater.forms import PcapForm


@login_required
def index(request):
    return render(request, 'index.html', {'form': PcapForm()})

@login_required
def timeline(request):
    id = request.GET['id']
    perfil = get_object_or_404(Perfil, pk=id)
    return render(request, 'timeline.html', {'perfil': perfil})

@login_required
def apps(request):
    id = request.GET['id']
    link = get_object_or_404(Link, pk=id)
    return render(request, 'apps.html', {'link': link})

@login_required
def perfil(request):
    id = request.GET['id']
    perfil = get_object_or_404(Perfil, pk=id)
    return render(request, 'perfil.html', {'perfil': perfil})
















