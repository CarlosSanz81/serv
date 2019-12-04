from django.shortcuts import render
import sys, os
from django.http import HttpResponseRedirect


from .forms import FormArchivo
from .models import Pedido, Archivo
from bd.models import Libro
# from .somewhere import handle_uploaded_file



# Create your views here.

def grabar_pedido(arch):
    print('Hola')
    print(arch)
    print(arch.pedido)
    print(arch.libro)
    identidad = Libro.objects.get(isbn = arch.libro)
    print(identidad.id)
    print(arch.copias)
    
    insert = Pedido(
        estado = False,
        id_cliente_id= 1,
        pedido_cliente = str(arch.pedido),
        pedido_interno = 0,
        id_libro_id = int(identidad.id),
        copias = int(arch.copias),
        uc_id = 1
        )
    print(insert)
    insert.save()


def ped(arch, archivo):
    print('Arch {}'.format(arch))
    ruta = 'media/' + str(arch)
    print ('Rutas: {}'.format(ruta))
    
    pedido = open(ruta, 'r')
    
    datos = pedido.readlines()
    pedidos = []
    
    contador = 0

    for linea in datos:
        lineas = linea.split('\t')
        if lineas[0] == '3':
            contador = contador + 1
    print(contador)
    isbns = []
    copiass = []
    numero_pedido = ''
    for linea in datos:
        lineas = linea.split('\t')
        if lineas[0] == '1':
            numero_pedido = lineas[4]
            print('Pedido = {}'.format(numero_pedido))
        if lineas[0] == '3':
            if contador == 1:
                isbn = lineas[1]
                copias = lineas[2]
                print('Numero de pedido: {}'.format(numero_pedido))
                print('ISBN: {} - {} copias'.format(isbn, copias))
                
            else:
                isbn = lineas[1]
                isbns.append(isbn)
                copias = lineas[2]
                copiass.append(copias) 
                
    if contador == 1:
        archivo.pedido = numero_pedido
        archivo.copias = copias
        archivo.libro = isbn
        archivo.save()
       
    else:
        isb = ''
        cop = ''
        for i in range(contador):          
            isb = isb + '//' + isbns[i]
            cop = cop + '//' + str(copiass[i])
        archivo.pedido = numero_pedido
        archivo.copias = cop
        archivo.libro = isb
        archivo.save()
        
    print('adios')
    print(archivo.id)
    
    grabar_pedido(archivo)
    
    return render(request, 'pedidos/importar.html',{'error_message': "Archivo: {} subido correctamente".format(arch),})




def importarpedido(request):
    if request.method == 'GET':

        return render(request, 'pedidos/importar.html')
    if request.method == 'POST':
        form = FormArchivo(request.POST, request.FILES)
        try:
            if form.is_valid():
                arch = request.FILES['gol']
                ruta = 'media/' + str(arch)
                if os.path.exists(ruta):
                    print('El Archivo Existe ya')
                    return render(request, 'pedidos/importar.html',{'error_message': "El archivo ya ha sido subido",})
                else:
                    insert = Archivo(arch=arch)
                    
                    insert.save()
                    print('Correcto')
                    
                    ped(arch, insert)
                    
                    
        except:
            return render(request, 'pedidos/importar.html',{'error_message': "Selecciona un Archivo",})      
            
    return render(request, 'pedidos/importar.html')






