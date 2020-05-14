# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    num_detalle = models.FloatField(primary_key=True)
    nro_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='nro_factura')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_factura'
        unique_together = (('num_detalle', 'nro_factura'),)


class DetalleOrden(models.Model):
    num_detalle = models.FloatField(primary_key=True)
    id_orden = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_orden')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        unique_together = (('num_detalle', 'id_orden'),)


class DetalleVenta(models.Model):
    num_detalle = models.FloatField(primary_key=True)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('num_detalle', 'id_venta'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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

    class Meta:
        managed = False
        db_table = 'producto'


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


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'venta'
