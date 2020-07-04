from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.db.models import Count

from .forms import *
from .models import *


# Create your views here.

# Home
def home(request):
    producto = Producto.objects.all()
    categoria = CatProducto.objects.all()
    formulario = VentaForm
    data = {
        'productos': producto,
        'categorias': categoria,
        'formulario': formulario
    }

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_usuario = request.user
            post.save()
            return redirect(to='AgregarDetalleVenta')
        else:
            print('formulario incorrecto')
        data['form'] = form
    return render(request, 'core/home.html', data)


# User registration and login
class registro_usuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'registration/registrar.html'
    success_url = reverse_lazy('registration_done')


def registration_done(request):
    return render(request, 'registration/registration_done.html')


# Product module
@method_decorator(login_required, name='dispatch')
class registro_producto(CreateView):
    model = ProductoTemp
    form_class = ProductoForm
    template_name = 'core/productos/registro_producto.html'
    success_url = reverse_lazy('ListaProductos')


@method_decorator(login_required, name='dispatch')
class ProductEdit(UpdateView):
    model = Producto
    form_class = ProductoFormEdit
    template_name = 'core/productos/registro_producto.html'
    success_url = reverse_lazy('ListaProductos')


@method_decorator(login_required, name='dispatch')
class ProductList(ListView):
    model = Producto
    template_name = 'core/productos/lista_productos.html'


@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Producto
    template_name = 'core/productos/eliminar_producto.html'
    success_url = reverse_lazy('ListaProductos')


# nuevo detalle producto
def detalle_producto(request, indice):
    data = {
        'producto': Producto.objects.get(id_producto=indice)
    }

    return render(request, 'core/productos/detalle_producto.html', data)


# Ordenes de compra
def orden_admin(request):
    formulario = OrdenForm()
    data = {
        'lista': OrdenCompra.objects.all(),
        'formulario': formulario
    }

    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_usuario = request.user
            post.save()
            return redirect(to='RegistroDetalle')
        data['form'] = form

    return render(request, 'core/orden_compra/orden_admin.html', data)


@method_decorator(login_required, name='dispatch')
class RegistroDetalleOrden(CreateView):
    model = DetalleOrden
    form_class = DetalleOrdenForm
    template_name = 'core/orden_compra/detalle_orden.html'
    success_url = reverse_lazy('RegistroDetalle')

    def post(self, request, *args, **kwargs):
        form = DetalleOrdenForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            index = OrdenCompra.objects.filter(id_usuario=request.user).order_by('-id_orden')[:1]
            precio = Producto.objects.filter(nombre=post.id_producto).values('precio_unit')
            post.id_orden = index.first()
            post.precio_unit = precio
            post.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form', form})


@method_decorator(login_required, name='dispatch')
class OrdenList(ListView):
    model = OrdenCompra
    template_name = 'core/orden_compra/lista_ordenes.html'

    def get_queryset(self):
        return OrdenCompra.objects.filter(id_proveedor=self.request.user.id_usuario)


@login_required
def detalle_orden_list(request, indice, est):
    detalles = DetalleOrden.objects.filter(id_orden=indice)
    detextra = DetalleOrdenForm
    data = {
        'detalles': detalles,
        'index': indice,
        'estado': est,
        'formulario': detextra,
    }

    if request.method == 'POST':
        form = DetalleOrdenForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            indice = OrdenCompra.objects.filter(id_orden=indice)
            post.id_orden = indice.first()
            post.save()
            return redirect(to='AdminOrdenes')
        data['form'] = form

    return render(request, 'core/orden_compra/Orden_Seleccionada.html', data)


@method_decorator(login_required, name='dispatch')
class OrdenDelete(DeleteView):
    model = OrdenCompra
    template_name = 'core/orden_compra/eliminar_orden.html'
    success_url = reverse_lazy('AdminOrdenes')


@method_decorator(login_required, name='dispatch')
class OrdenEdit(UpdateView):
    model = OrdenCompra
    form_class = OrdenEditForm
    template_name = 'core/orden_compra/editar_orden.html'
    success_url = reverse_lazy('AdminOrdenes')


# Modulo factura
@login_required
def factura_admin(request):
    formulario = FacturaForm
    data = {
        'lista': Factura.objects.all(),
        'formulario': formulario
    }
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='NuevoDetalleFact')  # <--  aqui va la vista de los detalles
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


@method_decorator(login_required, name='dispatch')
class FacturaListCliente(ListView):
    model = Factura
    template_name = 'core/facturas/facturas_cliente.html'

    def get_queryset(self):
        return Factura.objects.filter(id_usuario=self.request.user.id_usuario)


# Modulo boleta
@login_required
def boleta_admin(request):
    formulario = BoletaForm()
    data = {
        'lista': Boleta.objects.all(),
        'formulario': formulario
    }

    if request.method == 'POST':
        form = BoletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='RegistroDetalleBoleta')
        data['form'] = form

    return render(request, 'core/boletas/listado_boletas.html', data)


@method_decorator(login_required, name='dispatch')
class RegistroDetalleBoleta(CreateView):
    model = DetalleBoleta
    form_class = DetalleBoletaForm
    template_name = 'core/boletas/detalle_boleta.html'
    success_url = reverse_lazy('RegistroDetalleBoleta')

    def post(self, request, *args, **kwargs):
        form = DetalleBoletaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, {'form', form})


@login_required
def detalle_boleta_list(request, indice):
    detalles = DetalleBoleta.objects.filter(nro_boleta=indice)
    data = {
        'detalles': detalles,
        'index': indice
    }

    return render(request, 'core/boletas/boleta_seleccionada.html', data)


@method_decorator(login_required, name='dispatch')
class BoletaListCliente(ListView):
    model = Boleta
    template_name = 'core/boletas/boletas_cliente.html'

    def get_queryset(self):
        return Boleta.objects.filter(id_usuario=self.request.user.id_usuario)


@method_decorator(login_required, name='dispatch')
class BoletaAnular(UpdateView):
    model = Boleta
    form_class = EditBoletaForm
    template_name = 'core/boletas/anular_boleta.html'
    success_url = reverse_lazy('AdminBoletas')


# Vista proveedores
@method_decorator(login_required, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'core/administracion/lista_proveedores.html'


# Vista para editar detalles de orden
@method_decorator(login_required, name='dispatch')
class EditDetalleOrden(UpdateView):
    model = DetalleOrden
    form_class = EditDetOrdenForm
    template_name = 'core/orden_compra/editar_detalle_orden.html'
    success_url = reverse_lazy('AdminOrdenes')


# Vista listado personal
@method_decorator(login_required, name='dispatch')
class ListadoPersonal(ListView):
    model = Usuario
    template_name = 'core/administracion/listado_personal.html'

    def get_queryset(self):
        return Usuario.objects.filter(is_staff=True)


# Modulo de ventas
@login_required
def venta_admin(request):
    formulario = VentaForm()
    data = {
        'lista': Venta.objects.all(),
        'formulario': formulario
    }

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_usuario = request.user
            post.save()
            return redirect(to='AgregarDetalleVenta')
        data['form'] = form

    return render(request, 'core/ventas/ventas_admin.html', data)


def agregar_detalle_venta(request):
    form = DetalleVentaForm
    index = Venta.objects.filter(id_usuario=request.user).order_by('-id_venta')[:1]
    listaVacia = DetalleVenta.objects.filter(id_venta=index).count()
    data = {
        'form': form,
        'listaVacia': listaVacia
    }
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid() and form.save(commit=False).cantidad > 0:
            post = form.save(commit=False)
            index = Venta.objects.filter(id_usuario=request.user).order_by('-id_venta')[:1]
            precio = Producto.objects.filter(nombre=post.id_producto).values('precio_unit')
            post.id_venta = index.first()
            post.precio_unit = precio
            post.save()
            return redirect(to='AgregarDetalleVenta')
        data['form'] = form

    return render(request, 'core/ventas/detalle_venta.html', data)


@login_required
def detalle_venta_list(request, indice):
    detalles = DetalleVenta.objects.filter(id_venta=indice)
    data = {
        'detalles': detalles,
        'index': indice
    }

    return render(request, 'core/ventas/venta_seleccionada.html', data)


@method_decorator(login_required, name='dispatch')
class VentaEdit(UpdateView):
    model = Venta
    form_class = EditVentaForm
    template_name = 'core/ventas/editar_venta.html'
    success_url = reverse_lazy('VentasAdmin')


@method_decorator(login_required, name='dispatch')
class VentaDelete(DeleteView):
    model = Venta
    template_name = 'core/ventas/eliminar_venta.html'
    success_url = reverse_lazy('VentasAdmin')
