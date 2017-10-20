# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Establecimiento
from .forms import UserForm




class IndexView(generic.ListView):
    template_name = 'establecimientos/establecimientos.html'
    context_object_name = 'lista_estableciemiento'

    def get_queryset(self):
        return Establecimiento.objects.all()


class EstablecimientoCreate(CreateView):
    model = Establecimiento
    fields = ['nombre', 'nro', 'lat', 'long', 'regimen']
    success_url = reverse_lazy('establecimientos:listar')


class DetailView(generic.DetailView):
    model = Establecimiento
    template_name = 'establecimientos/detalle.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'establecimientos/registro_usuario.html'

    #Si no está logueado le va a mostrar una página en blanco
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            usuario = form.save(commit=False)

            #Se normalizan los datos con cleaned_data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()

            #Devuelve un objeto User si las credenciales son correctas
            usuario = authenticate(username=username, password=password)

            if usuario is not None:

                if usuario.is_active:

                    login(request, usuario)
                    return redirect('establecimientos:listar')

        return render(request, self.template_name, {'form': form})



