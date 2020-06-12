from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario.as_view(), name="registro_usuario"),
    path('registro/done', registration_done, name="registration_done"),
    path('orden/', RegistroOrden.as_view(), name="RegistroOrden"),
    path('detalleorden/', RegistroDetalleOrden.as_view(), name="RegistroDetalle"),
    path('lista_proveedores/', ProveedorListView.as_view(), name="ListaProveedor"),
    path('productos/new', registro_producto.as_view(), name="registro_producto"),
    path('productos/list', ProductList.as_view(), name="ListaProductos"),
    path('productos/edit/<str:pk>/', ProductEdit.as_view(), name="EditarProductos"),
    path('productos/delete/<str:pk>/', ProductDelete.as_view(), name="EliminarProductos"),
]

