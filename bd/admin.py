from django.contrib import admin
from .models import Libro, Formato_Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro

class LibroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_field = ['isbn', 'cod_interno', 'cod_cliente', 'titulo']
    list_display = ('id','isbn','titulo','cod_cliente','cod_interno','no_paginas','dato_variable','id_formato_libro','id_papel','solapas','paginas_bitono','paginas_color','paginas_bn','id_modo','id_cliente','tamaño_lomo','tamaño_portada','tamaño_portada_sangre','no_impresiones','coste','venta','estado','uc','um')
    resource_class = LibroResource

class Formato_LibroAdmin(admin.ModelAdmin):
    search_field = ['formatotxt']
    list_display = ('formatotxt','ancho', 'largo')

admin.site.register(Libro, LibroAdmin)
admin.site.register(Formato_Libro, Formato_LibroAdmin)