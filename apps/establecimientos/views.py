# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Establecimiento
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'establecimientos/establecimientos.html'
    context_object_name = 'lista_estableciemiento'

    def get_queryset(self):
        return Establecimiento.objects.all()


class EstablecimientoCreate(CreateView):
    model = Establecimiento
    fields = ['nombre', 'nro', 'lat', 'long', 'regimen']
    success_url = reverse_lazy('establecimientos:index')
