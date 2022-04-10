from django import forms
from ckeditor.fields import RichTextFormField

class CerrajeroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    desempleado = forms.BooleanField(required=False)
    tarjeta_presentacion = RichTextFormField(required=False)

class CerrajeroBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)
    