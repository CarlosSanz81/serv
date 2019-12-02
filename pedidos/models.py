from django.db import models
from bases.models import ClaseModelo
from bd.models import Cliente, Libro

# Create your models here.
class Pedido(ClaseModelo):
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    pedido_cliente = models.CharField(max_length = 100, unique = True)
    pedido_interno = models.CharField(max_length = 100, blank = True)
    fecha_entrega =  models.DateTimeField( blank = True)
    id_libro = models.ForeignKey(Libro, on_delete= models.CASCADE)
    copias = models.IntegerField(default = 0)

    def __str__(self):
        return '{}'.format(self.pedido_cliente)
    
    def save(self):
        # self.id_libro = self.Cliente.isbn
        super(Pedido, self).save()

    class Meta:
        verbose_name_plural = "Pedidos"

class Archivo(models.Model):
    copias = models.CharField(max_length = 100, blank = True, null = True)
    pedido = models.CharField(max_length = 100, blank = True, null = True)
    arch = models.FileField(upload_to="media/", null=True, blank=True, unique= True)

    # def __str__(self):
    #     return '{}'.format(self.arch)
    
    # def save(self):
    #     # self.id_libro = self.Cliente.isbn
    #     super(Archivo, self).save()

    class Meta:
        verbose_name_plural = "Archivos"