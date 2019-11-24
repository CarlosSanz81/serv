from django.db import models
from django.core.exceptions import ValidationError

from bases.models import ClaseModelo

class Cliente(ClaseModelo):
    nombre = models.CharField(
        max_length = 100,
        unique = True
        )
    cif = models.CharField(
        max_length = 9,
        unique = True
        )
    direccion_fiscal = models.CharField(
        max_length = 200, 
        blank = True,  
        null = True
        )
    telefono = models.CharField(
        max_length = 10,
        null = True,
        blank = True
        )
    email = models.EmailField(max_length = 255, unique = False)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Clientes"
    
class TipoPapel(ClaseModelo):
    nombre = models.CharField(max_length = 100, unique = True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(TipoPapel, self).save()

    class Meta:
        verbose_name = "Tipo Papel"
        verbose_name_plural = "Tipos Papeles"

class Gramaje(ClaseModelo):
    gr = models.IntegerField(blank=False)
    def __str__(self):
        return '{}'.format(self.gr)
    
    def save(self):
        super(Gramaje, self).save()

    class Meta:
        verbose_name = "Gramaje"
        verbose_name_plural = "Gramajes"

class Papel(ClaseModelo):
    gr = models.ForeignKey(Gramaje, on_delete=models.CASCADE)
    tipopapel = models.ForeignKey(TipoPapel, on_delete=models.CASCADE)
    mano = models.FloatField(default = 1.2, blank=True)

    def __str__(self):
        return '{}:{}gr -{} mano'.format(self.tipopapel, self.gr, self.mano)
    
    def save(self):
        
        self.observaciones = str(self.tipopapel)+':'+str(self.gr)+'gr.-'+str(self.mano)+' mano'
        super(Papel, self).save()

    class Meta:
        verbose_name = "Papel"
        verbose_name_plural = "Papeles"

class Formato_Libro(ClaseModelo):
    formatotxt = models.CharField(
        max_length = 50, 
        blank = False, 
        null= False
        )
    ancho = models.FloatField(default = 0)
    largo = models.FloatField(default = 0)

    def __str__(self):
        return '{}'.format(self.formatotxt)
    
    def save(self):
        self.formatotxt = self.formatotxt.upper()
        self.formatotxt = self.formatotxt.replace(",",".")
        separar = self.formatotxt.split('X')
        self.ancho = float(separar[0])
        self.largo = float(separar[1])
        super(Formato_Libro, self).save()

    class Meta:
        verbose_name = "Formato Libro"
        verbose_name_plural = "Formatos Libro"

class Modo(ClaseModelo):
    nombre= models.CharField(
        max_length = 50,
        blank = False,
        null = False
    )

    def __str__(self):
        self.nombre= self.nombre.upper()
        return '{}'.format(self.nombre)

    def save(self):
        super(Modo, self).save()
    
    class Meta:
        verbose_name = 'Modo'
        verbose_name_plural = 'Modos'

class Contacto(ClaseModelo):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length = 50,
        blank = False,
        null = False
    )
    apellidos = models.CharField(
        max_length = 200,
        blank = True
    )
    tel_fijo = models.CharField(max_length = 9,blank=True)
    tel_fijo_ext = models.CharField(max_length = 9,blank=True)
    tel_personal = models.CharField(max_length = 9,blank=True)
    email = models.CharField(
        max_length = 200,
        blank = True
    )
    def __str__(self):
        return '{}:{}'.format(self.Cliente.nombre, self.nombre)
    
    def save(self):
        super(Contacto, self).save()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

class Libro(ClaseModelo):
    isbn = models.BigIntegerField(
        unique = True
        )
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
        blank = True
        )
    no_paginas = models.IntegerField(default = 0)
    dato_variable = models.BooleanField(default= False)
    id_formato_libro = models.ForeignKey(Formato_Libro, on_delete=models.CASCADE)
    id_papel= models.ForeignKey(Papel, on_delete=models.CASCADE)
    solapas= models.BooleanField(default= False)
    paginas_bitono= models.IntegerField(default=0)
    paginas_color= models.IntegerField(default=0)
    paginas_bn=models.IntegerField(default=0)
    id_modo=models.ForeignKey(Modo, on_delete=models.CASCADE)
    id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tamaño_lomo= models.FloatField(default = 0)
    tamaño_portada = models.FloatField(default = 0)
    tamaño_portada_sangre = models.FloatField(default = 0)
    no_impresiones= models.IntegerField(default=0)
    coste= models.FloatField(default = 0)
    venta= models.FloatField(default = 0)


    def __str__(self):
        return '{}'.format(self.isbn)

    

    def clean_isbn(self):
        data = self.cleaned_data['isbn']
            
        #Check date is not in past. 
        if data < 999999999999:
            raise ValidationError(_('ISBN invalido, le faltan dígitos'))
            #Check date is in range librarian allowed to change (+4 weeks).
        if data > 9999999999999:
            raise ValidationError(_('ISBN inválido, le sobran dígitos'))

        # Remember to always return the cleaned data.
        return data

    def save(self):
        super(Libro, self).save()
    
    class Meta:
        verbose_name_plural = "Libros"
        verbose_name = "Libro"

