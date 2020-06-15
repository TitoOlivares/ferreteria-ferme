from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .forms import *
from .models import *


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
    success_url = reverse_lazy('ListaProductos')


def orden_admin(request):
    formulario = OrdenForm()
    data = {
        'lista': OrdenCompra.objects.all(),
        'formulario': formulario
    }

    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='RegistroDetalle')
        data['form'] = form

    return render(request, 'core/orden_compra/orden_admin.html', data)


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
    template_name = 'core/orden_compra/lista_ordenes.html'

    def get_queryset(self):
        return OrdenCompra.objects.filter(id_proveedor=self.request.user.id_usuario)


@login_required
def detalle_orden_list(request, indice):
    detalles = DetalleOrden.objects.filter(id_orden=indice)
    data = {
        'detalles': detalles,
        'index': indice
    }

    return render(request, 'core/orden_compra/Orden_Seleccionada.html', data)


@method_decorator(login_required, name='dispatch')
class DetalleProducto(UpdateView):
    model = Producto
    form_class = ProductoFormEdit
    template_name = 'core/productos/detalle_producto.html'


@method_decorator(login_required, name='dispatch')
class OrdenDelete(DeleteView):
    model = OrdenCompra
    template_name = 'core/orden_compra/eliminar_orden.html'
    success_url = reverse_lazy('AdminOrdenes')

@login_required
def factura_admin(request):
    formulario= FacturaForm
    data = {
        'lista': Factura.objects.all(),
        'formulario': formulario
    }
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='NuevoDetalleFact')   #<--  aqui va la vista de los detalles
        data['form'] = form

    return render(request, 'core/facturas/factura_admin.html', data)


class NuevoDetalleFactura(CreateView):
    model = DetalleFactura
    form_class = DetalleFacturaForm
    template_name = 'core/facturas/detalle_factura.html'
    success_url = reverse_lazy('NuevoDetalleFact')

    def post(self, request, *args, **kwargs):
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form', form})


@login_required
def detalle_fact_list(request, indice):
    detalles = DetalleFactura.objects.filter(nro_factura=indice)
    data = {
        'detalles': detalles,
        'index': indice
    }

    return render(request, 'core/facturas/factura_seleccionada.html', data)


@method_decorator(login_required, name='dispatch')
class FacturaAnular(UpdateView):
    model = Factura
    form_class = EditFacturaForm
    template_name = 'core/facturas/anular_factura.html'
    success_url = reverse_lazy('AdminFactura')