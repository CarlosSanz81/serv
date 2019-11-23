from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Cliente, TipoPapel, Gramaje, Papel, Formato_Libro, Modo, Contacto
from .forms import ClienteForm, TipoPapelForm, GramajeForm, PapelForm, Formato_LibroForm, ModoForm, ContactoForm

from bases.views import SinPrivilegios
from django.http import HttpResponse

#CLIENTES
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_cliente"
    model = Cliente
    template_name = "bd/cliente_list.html"
    context_object_name = "obj"

class ClienteNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Cliente
    template_name = "bd/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("bd:cliente_list")
    success_message = "Cliente Creado"
    permission_required ="bd.add_cliente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ClienteEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Cliente
    template_name = "bd/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("bd:cliente_list")
    success_message = "Cliente Actualizado Correctamente"
    permission_required = "bd.change_cliente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#TIPOS DE PAPEL
class TipoPapelView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_tipopapel"
    model = TipoPapel
    template_name = "bd/tipopapel_list.html"
    context_object_name = "obj"

class TipoPapelNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = TipoPapel
    template_name = "bd/tipopapel_form.html"
    context_object_name = "obj"
    form_class = TipoPapelForm
    success_url = reverse_lazy("bd:tipopapel_list")
    success_message = "Tipo de Papel Creado"
    permission_required ="bd.add_tipopapel"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class TipoPapelEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = TipoPapel
    template_name = "bd/tipopapel_form.html"
    context_object_name = "obj"
    form_class = TipoPapelForm
    success_url = reverse_lazy("bd:tipopapel_list")
    success_message = "Tipo de Papel Actualizado Correctamente"
    permission_required = "bd.change_tipopapel"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#GRAMAJES
class GramajeView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_gramaje"
    model = Gramaje
    template_name = "bd/gramaje_list.html"
    context_object_name = "obj"

class GramajeNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Gramaje
    template_name = "bd/gramaje_form.html"
    context_object_name = "obj"
    form_class = GramajeForm
    success_url = reverse_lazy("bd:gramaje_list")
    success_message = "Tipo de Papel Creado"
    permission_required ="bd.add_gramaje"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class GramajeEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Gramaje
    template_name = "bd/gramaje_form.html"
    context_object_name = "obj"
    form_class = GramajeForm
    success_url = reverse_lazy("bd:gramaje_list")
    success_message = "Tipo de Papel Actualizado Correctamente"
    permission_required = "bd.change_gramaje"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#PAPELES
class PapelView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_papel"
    model = Papel
    template_name = "bd/papel_list.html"
    context_object_name = "obj"

class PapelNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Papel
    template_name = "bd/papel_form.html"
    context_object_name = "obj"
    form_class = PapelForm
    success_url = reverse_lazy("bd:papel_list")
    success_message = "Tipo de Papel Creado"
    permission_required ="bd.add_papel"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PapelEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Papel
    template_name = "bd/papel_form.html"
    context_object_name = "obj"
    form_class = PapelForm
    success_url = reverse_lazy("bd:papel_list")
    success_message = "Tipo de Papel Actualizado Correctamente"
    permission_required = "bd.change_papel"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#FORMATO
class Formato_LibroView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_formato_libro"
    model = Formato_Libro
    template_name = "bd/formato_libro_list.html"
    context_object_name = "obj"

class Formato_LibroNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Formato_Libro
    template_name = "bd/formato_libro_form.html"
    context_object_name = "obj"
    form_class = Formato_LibroForm
    success_url = reverse_lazy("bd:formato_libro_list")
    success_message = "Formato Creado"
    permission_required ="bd.add_formato_libro"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class Formato_LibroEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Formato_Libro
    template_name = "bd/formato_libro_form.html"
    context_object_name = "obj"
    form_class = Formato_LibroForm
    success_url = reverse_lazy("bd:formato_libro_list")
    success_message = "Formato Actualizado Correctamente"
    permission_required = "bd.change_cliente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


#MODO
class ModoView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_modo"
    model = Modo
    template_name = "bd/modo_list.html"
    context_object_name = "obj"

class ModoNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Modo
    template_name = "bd/modo_form.html"
    context_object_name = "obj"
    form_class = ModoForm
    success_url = reverse_lazy("bd:modo_list")
    success_message = "Formato Creado"
    permission_required ="bd.add_modo"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ModoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Modo
    template_name = "bd/modo_form.html"
    context_object_name = "obj"
    form_class = ModoForm
    success_url = reverse_lazy("bd:modo_list")
    success_message = "Formato Actualizado Correctamente"
    permission_required = "bd.change_cliente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#CLIENTES
class ContactoView(SinPrivilegios, generic.ListView):
    permission_required = "bd.view_contacto"
    model = Contacto
    template_name = "bd/contacto_list.html"
    context_object_name = "obj"

class ContactoNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Contacto
    template_name = "bd/contacto_form.html"
    context_object_name = "obj"
    form_class = ContactoForm
    success_url = reverse_lazy("bd:contacto_list")
    success_message = "Contacto Creado"
    permission_required ="bd.add_contacto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ContactoEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Contacto
    template_name = "bd/contacto_form.html"
    context_object_name = "obj"
    form_class = ContactoForm
    success_url = reverse_lazy("bd:contacto_list")
    success_message = "Contacto Actualizado Correctamente"
    permission_required = "bd.change_contacto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

#INACTIVACIONES
@login_required(login_url = '/login/')
@permission_required('bd.change_cliente', login_url= 'bases:sin_privilegios')
def cliente_inactivar(request, id):
    template_name = "bd/cliente_inactivar.html"
    contexto={}
    cliente = Cliente.objects.filter(pk=id).first()
    
    if not cliente:
        return HttpResponse('Cliente no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':cliente}
    
    if request.method == 'POST':
        if cliente.estado:
            cliente.estado = False
            cliente.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Cliente Inactivado')
            
        else:
            cliente.estado = True
            cliente.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Cliente Activado')
    return render(request, template_name,contexto)

@login_required(login_url = '/login/')
@permission_required('bd.change_tipopapel', login_url= 'bases:sin_privilegios')
def tipopapel_inactivar(request, id):
    template_name = "bd/tipopapel_inactivar.html"
    contexto={}
    tipopapel = TipoPapel.objects.filter(pk=id).first()
    
    if not tipopapel:
        return HttpResponse('Tipo de Papel no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':tipopapel}
    
    if request.method == 'POST':
        if tipopapel.estado:
            tipopapel.estado = False
            tipopapel.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Tipo de Papel Inactivado')
            
        else:
            tipopapel.estado = True
            tipopapel.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Tipo de Papel Activado')
    return render(request, template_name,contexto)

@login_required(login_url = '/login/')
@permission_required('bd.change_gramaje', login_url= 'bases:sin_privilegios')
def gramaje_inactivar(request, id):
    template_name = "bd/gramaje_inactivar.html"
    contexto={}
    gramaje = Gramaje.objects.filter(pk=id).first()
    
    if not gramaje:
        return HttpResponse('Gramaje no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':gramaje}
    
    if request.method == 'POST':
        if gramaje.estado:
            gramaje.estado = False
            gramaje.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Gramaje Inactivado')
            
        else:
            gramaje.estado = True
            gramaje.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Gramaje Activado')
    return render(request, template_name,contexto)

@login_required(login_url = '/login/')
@permission_required('bd.change_gramaje', login_url= 'bases:sin_privilegios')
def papel_inactivar(request, id):
    template_name = "bd/papel_inactivar.html"
    contexto={}
    papel = Papel.objects.filter(pk=id).first()
    
    if not papel:
        return HttpResponse('Papel no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':papel}
    
    if request.method == 'POST':
        if papel.estado:
            papel.estado = False
            papel.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Papel Inactivado')
            
        else:
            papel.estado = True
            papel.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Papel Activado')
    return render(request, template_name,contexto)

@login_required(login_url = '/login/')
@permission_required('bd.change_formato_libro', login_url= 'bases:sin_privilegios')
def formato_libro_inactivar(request, id):
    template_name = "bd/formato_libro_inactivar.html"
    contexto={}
    formato_libro = Formato_Libro.objects.filter(pk=id).first()
    
    if not formato_libro:
        return HttpResponse('Formato no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':formato_libro}
    
    if request.method == 'POST':
        if formato_libro.estado:
            formato_libro.estado = False
            formato_libro.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Formato Inactivado')
            
        else:
            formato_libro.estado = True
            formato_libro.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Formato Activado')
    return render(request, template_name,contexto)


@login_required(login_url = '/login/')
@permission_required('bd.change_modo', login_url= 'bases:sin_privilegios')
def modo_inactivar(request, id):
    template_name = "bd/modo_inactivar.html"
    contexto={}
    modo = Modo.objects.filter(pk=id).first()
    
    if not modo:
        return HttpResponse('Modo no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':modo}
    
    if request.method == 'POST':
        if modo.estado:
            modo.estado = False
            modo.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Modo Inactivado')
            
        else:
            modo.estado = True
            modo.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Modo Activado')
    return render(request, template_name,contexto)

#INACTIVACIONES
@login_required(login_url = '/login/')
@permission_required('bd.change_contacto', login_url= 'bases:sin_privilegios')
def contacto_inactivar(request, id):
    template_name = "bd/contacto_inactivar.html"
    contexto={}
    contacto = Contacto.objects.filter(pk=id).first()
    
    if not contacto:
        return HttpResponse('Contacto no existe ' + str(id))

    if request.method == 'GET':
        contexto = {'obj':contacto}
    
    if request.method == 'POST':
        if contacto.estado:
            contacto.estado = False
            contacto.save()
            contexto = {'obj':'OK'}
            
            return HttpResponse('Contacto Inactivado')
            
        else:
            contacto.estado = True
            contacto.save()
            contexto = {'obj':'OK'}
            return HttpResponse('Contacto Activado')
    return render(request, template_name,contexto)