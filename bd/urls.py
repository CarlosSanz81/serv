from django.urls import path

from .views import ClienteView, ClienteNew, ClienteEdit, cliente_inactivar, \
                    TipoPapelView, TipoPapelNew, TipoPapelEdit, tipopapel_inactivar, \
                    GramajeView, GramajeNew, GramajeEdit, gramaje_inactivar, \
                    PapelView, PapelNew, PapelEdit, papel_inactivar, \
                    Formato_LibroView, Formato_LibroNew, Formato_LibroEdit, formato_libro_inactivar, \
                    ModoView, ModoNew, ModoEdit, modo_inactivar, \
                    ContactoView, ContactoNew, ContactoEdit, contacto_inactivar, \
                    LibroView, LibroNew, LibroEdit, libro_inactivar

urlpatterns = [
    # CLIENTES
    path('clientes/', ClienteView.as_view(), name = 'cliente_list'),
    path('clientes/new', ClienteNew.as_view(), name = 'cliente_new'),
    path('clientes/edit/<int:pk>', ClienteEdit.as_view(), name = 'cliente_edit'),
    path('clientes/incactivar/<int:id>', cliente_inactivar, name = 'cliente_inactivar'),

    # TIPOS DE PAPEL
    path('tipo_papeles/', TipoPapelView.as_view(), name = 'tipopapel_list'),
    path('tipo_papeles/new', TipoPapelNew.as_view(), name = 'tipopapel_new'),
    path('tipo_papeles/edit/<int:pk>', TipoPapelEdit.as_view(), name = 'tipopapel_edit'),
    path('tipo_papeles/incactivar/<int:id>', tipopapel_inactivar, name = 'tipopapel_inactivar'),

    # GRAMAJES
    path('gramajes/', GramajeView.as_view(), name = 'gramaje_list'),
    path('gramajes/new', GramajeNew.as_view(), name = 'gramaje_new'),
    path('gramajes/edit/<int:pk>', GramajeEdit.as_view(), name = 'gramaje_edit'),
    path('gramajes/incactivar/<int:id>', gramaje_inactivar, name = 'gramaje_inactivar'),

    # PAPELES
    path('papeles/', PapelView.as_view(), name = 'papel_list'),
    path('papeles/new', PapelNew.as_view(), name = 'papel_new'),
    path('papeles/edit/<int:pk>', PapelEdit.as_view(), name = 'papel_edit'),
    path('papeles/incactivar/<int:id>', papel_inactivar, name = 'papel_inactivar'),

    # FORMATO
    path('formatos_libros/', Formato_LibroView.as_view(), name = 'formato_libro_list'),
    path('formatos_libros/new', Formato_LibroNew.as_view(), name = 'formato_libro_new'),
    path('formatos_libros/edit/<int:pk>', Formato_LibroEdit.as_view(), name = 'formato_libro_edit'),
    path('formatos_libros/incactivar/<int:id>', formato_libro_inactivar, name = 'formato_libro_inactivar'),

    # MODO
    path('modos/', ModoView.as_view(), name = 'modo_list'),
    path('modos/new', ModoNew.as_view(), name = 'modo_new'),
    path('modos/edit/<int:pk>', ModoEdit.as_view(), name = 'modo_edit'),
    path('modos/incactivar/<int:id>', modo_inactivar, name = 'modo_inactivar'),

    # CONTACTOS
    path('contactos/', ContactoView.as_view(), name = 'contacto_list'),
    path('contactos/new', ContactoNew.as_view(), name = 'contacto_new'),
    path('contactos/edit/<int:pk>', ContactoEdit.as_view(), name = 'contacto_edit'),
    path('contactos/incactivar/<int:id>', contacto_inactivar, name = 'contacto_inactivar'),

    # LIBROS
    path('libros/', LibroView.as_view(), name = 'libro_list'),
    path('libros/new', LibroNew.as_view(), name = 'libro_new'),
    path('libros/edit/<int:pk>', LibroEdit.as_view(), name = 'libro_edit'),
    path('libros/incactivar/<int:id>', libro_inactivar, name = 'libro_inactivar'),

   
]
