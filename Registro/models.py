# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido1=models.CharField(max_length=50)
    apellido2=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    contrasena=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre