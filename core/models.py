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
    total = models.FloatField()
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'boleta'

    def __str__(self):
        return 'Boleta nro ' + self.nro_boleta


class CatProducto(models.Model):
    id_categoria = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cat_producto'
        verbose_name_plural = 'Categorías de productos'

    def __str__(self):
        return self.nombre


class DetalleBoleta(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    nro_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='nro_boleta')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_boleta'
        verbose_name_plural = 'Detalles de boletas'

    def __str__(self):
        return 'Boleta nro ' + self.nro_boleta


class DetalleFactura(models.Model):
    nro_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='nro_factura')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_factura'
        verbose_name_plural = 'Detalles de facturas'

    def __str__(self):
        return 'Factura nro ' + self.nro_factura


class DetalleOrden(models.Model):
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_orden = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_orden')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        verbose_name_plural = 'Detalles órdenes de compra'

    def __str__(self):
        return 'Orden nro ' + self.id_orden


class DetalleVenta(models.Model):
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        verbose_name_plural = 'Detalles de ventas'

    def __str__(self):
        return 'Detalle de venta ' + self.id_venta


class EstadoOrden(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_orden'
        verbose_name_plural = 'Estados de órdenes'

    def __str__(self):
        return self.descripcion


class EstadoVenta(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_venta'
        verbose_name_plural = 'Estados de ventas'

    def __str__(self):
        return self.descripcion


class Factura(models.Model):
    nro_factura = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    razon_soc = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    contacto = models.IntegerField()
    neto = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'factura'

    def __str__(self):
        return 'Factura nro ' + self.nro_factura


class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    valor_total = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'orden_compra'
        verbose_name_plural = 'Órdenes de compras'

    def __str__(self):
        return 'Orden número ' + self.id_orden


class Perfil(models.Model):
    id_perfil = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.nombre


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

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class Recepcion(models.Model):
    id_recepcion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_orden = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_orden')

    class Meta:
        managed = False
        db_table = 'recepcion'
        verbose_name_plural = "Recepciones"
        unique_together = (('id_recepcion', 'id_orden'),)

    def __str__(self):
        return 'Recepción orden ' + self.id_orden


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=15)
    rut = models.CharField(unique=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.FloatField()
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=30)
    rubro = models.CharField(max_length=50, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    esempresa = models.FloatField()
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Venta(models.Model):
    id_venta = models.FloatField(primary_key=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'venta'

    def __str__(self):
        return self.id_venta
