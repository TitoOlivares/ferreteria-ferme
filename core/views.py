from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import UsuarioForm, ProductoForm, OrdenForm, DetalleOrdenForm, ProductoFormEdit
from .models import ProductoTemp, CatProducto, Usuario, Producto, OrdenCompra, DetalleOrden, Proveedor


# Create your views here.

def home(request):
    producto = Producto.objects.all()
    categoria = CatProducto.objects.all()
    data = {
        'productos': producto,
        'categorias': categoria,
    }
    return render(request, 'core/home.html', data)


class registro_usuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'registration/registrar.html'
    success_url = reverse_lazy('registration_done')


def registration_done(request):
    return render(request, 'registration/registration_done.html')


class registro_producto(CreateView):
    model = ProductoTemp
    form_class = ProductoForm
    template_name = 'core/registro_producto.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class ProductList(ListView):
    model = Producto
    template_name = 'core/lista_productos.html'

class ProductEdit(CreateView):
    model = Producto
    form_class = ProductoFormEdit
    template_name = 'core/registro_producto.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class RegistroOrden(CreateView):
    model = OrdenCompra
    form_class = OrdenForm
    template_name = 'core/registro_orden.html'
    success_url = reverse_lazy('RegistroDetalle')


@method_decorator(login_required, name='dispatch')
class RegistroDetalleOrden(CreateView):
    model = DetalleOrden
    form_class = DetalleOrdenForm
    template_name = 'core/detalle_orden.html'
    success_url = reverse_lazy('RegistroDetalle')


@method_decorator(login_required, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'core/lista_proveedores.html'

