from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

# from django.db import connection

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
    template_name = 'core/productos/registro_producto.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class ProductEdit(UpdateView):
    model = Producto
    form_class = ProductoFormEdit
    template_name = 'core/productos/registro_producto.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class RegistroOrden(CreateView):
    model = OrdenCompra
    form_class = OrdenForm
    template_name = 'core/orden_compra/registro_orden.html'
    success_url = reverse_lazy('RegistroDetalle')

    def post(self, request, *args, **kwargs):
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form', form})


@method_decorator(login_required, name='dispatch')
class ProductList(ListView):
    model = Producto
    template_name = 'core/productos/lista_productos.html'


@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Producto
    template_name = 'core/productos/eliminar_producto.html'
    success_url = reverse_lazy('ListaProductos')


@method_decorator(login_required, name='dispatch')
class RegistroDetalleOrden(CreateView):
    model = DetalleOrden
    form_class = DetalleOrdenForm
    template_name = 'core/orden_compra/detalle_orden.html'
    success_url = reverse_lazy('RegistroDetalle')

    def post(self, request, *args, **kwargs):
        form = DetalleOrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form', form})


@method_decorator(login_required, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'core/lista_proveedores.html'


@method_decorator(login_required, name='dispatch')
class OrdenList(ListView):
    model = OrdenCompra
    template_name = 'core/lista_ordenes.html'

    def get_queryset(self):
        return OrdenCompra.objects.filter(id_proveedor=self.request.user.id_usuario)


@login_required
def detalle_orden_list(request, indice):
    detalles = DetalleOrden.objects.filter(id_orden=indice)
    data ={
        'detalles':detalles,
        'index':indice
    }

    return render(request, 'core/Orden_Seleccionada.html', data)







# def filtro_orden( id_orden):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     out_cur = django_cursor.connection.cursor()
#
#     cursor.callproc('SP_LISTAR_DET_ORDEN()', [out_cur])
#
#     lista = []
#     for fila in out_cur:
#         lista.append(fila)
#
#     return(lista)
