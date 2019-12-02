from django import forms
from .models import Archivo
 
# class CustomClearableFileInput(ClearableFileInput):
#     template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
 
class FormEntrada(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']
        widgets = {
            'archivo': forms.TextInput
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

