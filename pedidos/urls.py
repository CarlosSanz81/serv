from django.urls import path

from .views import importarpedido

urlpatterns = [

    path('pedido/', importarpedido , name='importar_pedido'),
    

]