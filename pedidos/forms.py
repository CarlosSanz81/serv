from django import forms
from django.forms import ClearableFileInput
from .models import Pedido, Archivo
 
class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivo(forms.ModelForm):
    class Meta:
        model = Archivo
        error_message = ''
        fields = ['arch']
        widgets = {
            'arch': ClearableFileInput
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })


# class UploadFileForm(forms.Form):
#     file = forms.FileField()
