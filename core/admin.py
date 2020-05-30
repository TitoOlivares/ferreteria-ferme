from django.contrib import admin
from .models import Perfil, Usuario, Boleta, CatProducto, DetalleBoleta, DetalleFactura, DetalleOrden, DetalleVenta
from .models import EstadoOrden, EstadoVenta, Factura, OrdenCompra, Producto, Proveedor, Recepcion, Venta

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(Boleta)
admin.site.register(CatProducto)
admin.site.register(DetalleBoleta)
admin.site.register(DetalleFactura)
admin.site.register(DetalleOrden)
admin.site.register(DetalleVenta)
admin.site.register(EstadoOrden)
admin.site.register(EstadoVenta)
admin.site.register(Factura)
admin.site.register(OrdenCompra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Recepcion)
admin.site.register(Venta)