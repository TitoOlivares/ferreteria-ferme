from django.urls import path
from .views import home, registro_usuario, registration_done, registro_producto, RegistroOrden, RegistroDetalleOrden

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario.as_view(), name="registro_usuario"),
    path('registro/done', registration_done, name="registration_done"),
    path('nuevoproducto/', registro_producto.as_view(), name="registro_producto"),
    path('orden/', RegistroOrden.as_view(), name="RegistroOrden"),
    path('detalleorden/', RegistroDetalleOrden.as_view(), name="RegistroDetalle"),
]
