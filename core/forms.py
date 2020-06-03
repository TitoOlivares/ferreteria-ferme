from django.forms import ModelForm
from core.models import Usuario
from django.forms import *
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'rut', 'telefono', 'direccion', 'comuna', 'esempresa']
        widgets = {
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'correo@ejemplo.com'
                }
            ),
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Su primer nombre'
                }
            ),
            'apellido': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Su apellido paterno'
                }
            ),
            'rut': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '99999999-9'
                }
            ),
            'telefono': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '123456789',
                    'type': '-moz-appearance:textfield'
                }
            ),
            'direccion': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Calle, número'
                }
            ),
            'comuna': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ciudad'
                }
            ),
        }

