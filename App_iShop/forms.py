from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre...'}),
            'especificaciones': forms.TextInput(attrs={'placeholder':'Especificaciones...'}),
            'precio': forms.NumberInput(attrs={'placeholder':'Precio...'}),
            'imagen': forms.FileInput(),
        }

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto", max_length=30)
    
    
class FormularioEditarPerfil(UserChangeForm):
    
    # Oculto el campo password para que no se vea en el formulario
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), 
        required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class FormularioAvatar(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']