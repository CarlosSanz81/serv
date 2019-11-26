from django.shortcuts import render

from tablib import Dataset 

from .resources import Imp_LibroResource

# Create your views here.
def importar(request):  
    # template = loader.get_template('export/importar.html')  
    if request.method == 'POST':
        libro_resource = Imp_LibroResource()  
        dataset = Dataset()
        print('dataset')  #
        print(dataset)  
        nuevos_libros = request.FILES['xlsfile']
        print('nuevos_libros')   
        print(nuevos_libros)  # NOMBRE DEL ARCHIVO
        imported_data = dataset.load(nuevos_libros.read())
        print('imported_data') 
        print(imported_data) # TODOS LOS DATOS
        result = libro_resource.import_data(dataset, dry_run=True) # Test the data import  
        print('result.has_errors')  
        print(result.has_errors())  
        if not result.has_errors():
            libro_resource.import_data(dataset, dry_run=False) # Actually import now  
    return render(request, 'export/importar.html')