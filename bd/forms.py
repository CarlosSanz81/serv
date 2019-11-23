from django import forms

from .models import Cliente, TipoPapel, Gramaje, Papel, Formato_Libro, Modo, Contacto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cif', 'direccion_fiscal', 'telefono', 'email', 'estado']
        labels = {'nombre': 'Nombre',
                'cif':'CIF/NIF',
                'direccion_fiscal': 'Dirección',
                'telefono':'Teléfono',
                'email': 'Email',
                'estado': 'Estado'}
        widget = {'nombre': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class TipoPapelForm(forms.ModelForm):
    class Meta:
        model = TipoPapel
        fields = ['nombre', 'descripcion', 'estado']
        labels = {'nombre': 'Nombre',
                'descripcion':'Descripción',
                'estado': 'Estado'}
        widget = {'nombre': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class GramajeForm(forms.ModelForm):
    class Meta:
        model = Gramaje
        fields = ['gr', 'observaciones', 'estado']
        labels = {'gr': 'Gramaje',
                'observaciones': 'Observaciones',
                'estado': 'Estado'}
        widget = {'gr': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class PapelForm(forms.ModelForm):
    class Meta:
        model = Papel
        fields = ['tipopapel', 'gr', 'mano', 'observaciones', 'estado']
        labels = {'tipopapel': 'Tipo Papel',
                'gr': 'Gramaje',
                'mano': 'Mano',
                'observaciones': 'Nombre',
                'estado': 'Estado'}
                
        widget = {'observaciones': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['observaciones'].widget.attrs['readonly'] = True

class Formato_LibroForm(forms.ModelForm):
    class Meta:
        model = Formato_Libro
        fields = ['formatotxt', 'ancho', 'largo', 'estado']
        labels = {'formatotxt': 'Formato',
                'ancho': 'Ancho',
                'largo': 'Largo',
                'estado': 'Estado'}
                
        widget = {'formatotxt': forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['ancho'].widget.attrs['readonly'] = True
        self.fields['largo'].widget.attrs['readonly'] = True

class ModoForm(forms.ModelForm):
    class Meta:
        model = Modo
        fields = ['nombre', 'observaciones', 'estado']
        labels = {'nombre': 'Nombre',
                'observaciones':'Observaciones',
                'estado': 'Estado'}
        widget = {'nombre':forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['cliente', 'nombre', 'apellidos', 'tel_fijo', 'tel_fijo_ext',
                    'tel_personal', 'email', 'observaciones', 'estado']
        # labels = {'nombre': 'Nombre',
        #         'observaciones':'Observaciones',
        #         'estado': 'Estado'}
        widget = {'nombre':forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })