from django.shortcuts import render
import sys, os
from django.http import HttpResponseRedirect


from .forms import FormArchivo
from .models import Pedido, Archivo
# from .somewhere import handle_uploaded_file



# Create your views here.

def importarpedido(request):
    if request.method == 'POST':
        form = FormArchivo(request.POST, request.FILES)
        if form.is_valid():
            
            arch = request.FILES['gol']
            ruta = 'media/' + str(arch)
            if os.path.exists(ruta):
                print('El Archivo Existe ya')
            else:
                
                insert = Archivo(arch=arch)
                insert.save()
                datos = ped(arch)
                print('ID = {}'.format(insert))
                insert.pedido = datos[0]
                insert.copias = datos[1]
                    
                insert.save()    
            
    return render(request, 'pedidos/importar.html')


def ped(arch):
    ruta = 'media/' + str(arch)
    print ('Ruta: {}'.format(ruta))
    
    pedido = open(ruta, 'r')
    datos = pedido.readlines()
    pedidos = {}
    for linea in datos:

        lineas = linea.split('\t')
        print(lineas)

        if lineas[0] == '1':
            numero_pedido = lineas[4]
            print('Pedido = {}'.format(numero_pedido))


        if lineas[0] == '3':

            if lineas[1] in pedidos:
				
                valor = int(pedidos.get(lineas[1]))
                suma = valor + int(lineas[2])
                pedidos[lineas[1]] =  suma
            else:
                valor = lineas[1]
                pedidos[valor] = lineas[2]
    print('pedidos: {}'.format(pedidos))
    return numero_pedido, pedidos


def pedido(ped):
    insert = Pedido(id_cliente=1,
    pedido_cliente = ped[0],
    id_libro = 1,
    copias = 1)


