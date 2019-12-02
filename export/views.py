from django.shortcuts import render

from tablib import Dataset 

from .resources import Imp_LibroResource

from .models import Archivo
from .forms import FormEntrada
from bd.models import Libro
import openpyxl
import psycopg2
import datetime


# Create your views here.
def importar(request):
    if request.method == 'POST':
        form = FormEntrada(request.POST, request.FILES)
        if form.is_valid():
            arch = request.FILES['xlsfile']
            Archivo.archivo = arch
            # cab = cabecera(request, arch)
            # Archivo.cabecera = cab
            Archivo.save(self)
            
            
    return render(request, 'export/importar.html')

def cabecera(request, arch):
    print(arch)
    print(request)
    arch = Archivo.objects.filter(archivo = arch).first()
    ruta = 'media/' + str(arch)
    doc = openpyxl.load_workbook(arch)

    hojas = doc.sheetnames

    hoja = doc['Sheet1']
    contador = 1
    cab = []
    for fila in hoja.rows:
        if contador == 1:
            for celda in fila:
                cab.append(celda.value)
                contador += 1
        else:
            break
    return cab
    





    
    
    

