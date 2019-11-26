from django.db import models
from bases.models import ClaseModelo
from bd.models import Formato_Libro, Papel, Modo, Cliente

# Create your models here.
class Imp_Libro(models.Model):
    isbn = models.CharField(max_length=15, unique = True)
    titulo = models.CharField(
        max_length = 200,
        blank = True
        )
    cod_cliente = models.CharField(
        max_length = 200,
        blank = True
        )
    cod_interno = models.CharField(
        max_length = 200,
        blank = True,
        default = ''
        )
    no_paginas = models.IntegerField(default= 0)
    dato_variable = models.CharField(max_length = 10, default = 'no')
    formato_libro = models.CharField(max_length = 20, default= 'no hay formato')
    papel= models.CharField(max_length = 200, default = 'no hay papel')
    gramaje= models.IntegerField(default=0)
    solapas= models.CharField(max_length = 10, default = 'NO')
    paginas_bitono= models.IntegerField(default=0)
    paginas_color= models.IntegerField(default=0)
    paginas_bn = models.IntegerField(default=0)
    # id_modo=models.ForeignKey(Modo, on_delete=models.CASCADE, blank = True)
    id_cliente=models.CharField(max_length = 200, default = 'EDITORIAL SINTESIS, S.A.')
    # tamaño_lomo= models.FloatField(default = 0)
    # tamaño_portada = models.FloatField(default = 0)
    # tamaño_portada_sangre = models.FloatField(default = 0)
    # no_impresiones= models.IntegerField(default=0)
    # coste= models.FloatField(default = 0)
    # venta= models.FloatField(default = 0)
    estado = models.CharField(
        max_length = 10,
        blank = True
        )