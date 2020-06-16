from django.forms import ModelForm
from django import forms
from core.models import *
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


class ProductoFormEdit(ModelForm):
    class Meta:
        model = Producto
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
        fields = ['id_usuario', 'id_proveedor']


class DetalleOrdenForm(ModelForm):
    class Meta:
        model = DetalleOrden
        fields = ['id_orden', 'id_producto', 'cantidad', 'precio_unit']


class BoletaForm(ModelForm):
    class Meta:
        model = Boleta
        fields = ['id_usuario', 'id_venta']


class DetalleBoletaForm(ModelForm):
    class Meta:
        model = DetalleBoleta
        fields = ['nro_boleta', 'id_producto', 'cantidad', 'precio_unit']


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['razon_soc', 'giro', 'direccion', 'contacto', 'id_usuario', 'id_venta']


class DetalleFacturaForm(ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ['nro_factura', 'id_producto', 'cantidad', 'precio_unit']


class EditFacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['estado']


class EditBoletaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['estado']


class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_usuario']


class DetalleVentaForm(ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['id_venta', 'id_producto', 'cantidad', 'precio_unit']


class EditVentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['id_estado']
