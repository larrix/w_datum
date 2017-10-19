# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RegimenTenencia (models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Establecimiento (models.Model):
    nombre = models.CharField(max_length=50)
    nro = models.IntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    foto = models.FileField()
    regimen = models.ForeignKey(RegimenTenencia, on_delete=models.CASCADE)

    @property
    def __str__(self):
        return self.nombre



