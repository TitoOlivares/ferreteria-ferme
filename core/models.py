# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boleta(models.Model):
    nro_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'boleta'


class CatProducto(models.Model):
    id_categoria = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cat_producto'


class DetalleBoleta(models.Model):
    num_detalle = models.FloatField(primary_key=True)
    nro_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='nro_boleta')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_boleta'
        unique_together = (('num_detalle', 'nro_boleta'),)


class DetalleFactura(models.Model):
    num_detalle = models.FloatField()
    nro_factura = models.OneToOneField('Factura', models.DO_NOTHING, db_column='nro_factura', primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_factura'
        unique_together = (('nro_factura', 'num_detalle'),)


class DetalleOrden(models.Model):
    num_detalle = models.FloatField()
    id_orden = models.OneToOneField('OrdenCompra', models.DO_NOTHING, db_column='id_orden', primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        unique_together = (('id_orden', 'num_detalle'),)


class DetalleVenta(models.Model):
    num_detalle = models.FloatField()
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('id_venta', 'num_detalle'),)


class EstadoOrden(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_orden'


class EstadoVenta(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Factura(models.Model):
    nro_factura = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    razon_soc = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    contacto = models.IntegerField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'factura'


class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='id_estado')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Perfil(models.Model):
    id_perfil = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil'


class Producto(models.Model):
    id_producto = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio_unit = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    marca = models.CharField(max_length=50)
    fecha_venc = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(CatProducto, models.DO_NOTHING, db_column='id_categoria')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=12)
    telefono = models.FloatField()
    rubro = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Recepcion(models.Model):
    id_recepcion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_orden = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_orden')

    class Meta:
        managed = False
        db_table = 'recepcion'
        unique_together = (('id_recepcion', 'id_orden'),)


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=15)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=150)
    telefono = models.FloatField()
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=30)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    esempresa = models.FloatField()
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'usuario'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'venta'
