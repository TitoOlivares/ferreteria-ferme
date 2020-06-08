from django.forms import ModelForm
from core.models import Usuario, ProductoTemp, OrdenCompra
from django.forms import TextInput, EmailInput, NumberInput, DateInput, Textarea
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


class ProductoForm(ModelForm):
    class Meta:
        model = ProductoTemp
        fields = ['nombre', 'descripcion', 'precio_unit', 'stock', 'stock_critico', 'marca', 'fecha_venc',
                  'id_categoria', 'id_proveedor', 'url_img']
        widgets = {
            'fecha_venc': DateInput(
                attrs={
                    'class': 'datepicker'
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Max. 500 caracteres'
                }
            )
        }


class OrdenForm(ModelForm):
    class Meta:
        model = OrdenCompra
        fields = ['fecha', 'id_usuario', 'id_proveedor']
        widgets = {
            'fecha': DateInput(
                attrs={
                    'class': 'datepicker'
                }
            ),
        }
