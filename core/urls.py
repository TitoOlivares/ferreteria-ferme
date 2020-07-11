from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario.as_view(), name="registro_usuario"),
    path('registro/done', registration_done, name="registration_done"),
    path('lista_proveedores/', ProveedorListView.as_view(), name="ListaProveedor"),

    # urls productos
    path('productos/list', ProductList.as_view(), name="ListaProductos"),
    path('productos/new/', registro_producto.as_view(), name="registro_producto"),
    path('productos/edit/<str:pk>/', ProductEdit.as_view(), name="EditarProductos"),
    path('producto/detalle/<indice>', detalle_producto, name="DetalleProducto"),
    path('productos/delete/<str:pk>/', ProductDelete.as_view(), name="EliminarProductos"),

    # urls ordenes de compra
    path('admin_ordenes/', orden_admin, name="AdminOrdenes"),
    path('detalleorden/', RegistroDetalleOrden.as_view(), name="RegistroDetalle"),
    path('detalle_orden_list/<indice>/<est>', detalle_orden_list, name="DetallesOrden"),
    path('orden/delete/<int:pk>/', OrdenDelete.as_view(), name="EliminarOrden"),
    path('lista_ordenes/', OrdenList.as_view(), name="ListaOrdenes"),
    path('orden/editdetalle/<int:pk>/', EditDetalleOrden.as_view(), name="EditarDetalleOrden"),
    path('orden/edit/<int:pk>/', OrdenEdit.as_view(), name="OrdenEdit"),

    # urls Facturas
    path('admin_facturas/', factura_admin, name="AdminFactura"),
    path('detalle_factura/', NuevoDetalleFactura.as_view(), name="NuevoDetalleFact"),
    path('detalle_fact_list/<indice>/', detalle_fact_list, name="DetallesFactura"),
    path('facturas/anular/<int:pk>/', FacturaAnular.as_view(), name="AnularFactura"),
    path('misfacturas/', FacturaListCliente.as_view(), name="FacturasCliente"),

    # urls Boletas
    path('admin_boletas/', boleta_admin, name="AdminBoletas"),
    path('detalleboleta/', RegistroDetalleBoleta.as_view(), name="RegistroDetalleBoleta"),
    path('detalle_boleta_list/<indice>/', detalle_boleta_list, name="DetallesBoleta"),
    path('misboletas/', BoletaListCliente.as_view(), name="BoletasCliente"),
    path('boleta/anular/<int:pk>/', BoletaAnular.as_view(), name="AnularBoleta"),

    # Listado de personal
    path('admin/personal', ListadoPersonal.as_view(), name="ListadoPersonal"),

    ############ TEMPORAL VISTA DE COMPRAS CLIENTE ####################
    path('venta_admin/', venta_admin, name="VentasAdmin"),
    path('venta/detalle', agregar_detalle_venta, name="AgregarDetalleVenta"),
    path('venta/detalle/<indice>/', detalle_venta_list, name="DetallesVenta"),
    path('venta/edit/<int:pk>/', VentaEdit.as_view(), name="EditVenta"),
    path('venta/delete/<int:pk>/', VentaDelete.as_view(), name="EliminarVenta"),
    path('venta/confirm/<index>', confirmacion_venta, name="ConfirmacionVenta"),



    path('contacto/', contact_form, name="contact"),
    path('contacto/done', contact_form_done, name="contact_done"),

    path('despacho/', Despacho.as_view(), name="despacho"),
]
