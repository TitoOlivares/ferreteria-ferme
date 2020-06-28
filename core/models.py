# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class Boleta(models.Model):
    nro_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    estado = models.BooleanField(default=True, verbose_name='Desmarque esta casilla para anular la boleta')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', verbose_name='Cliente')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta', verbose_name='Nro Venta')

    class Meta:
        managed = False
        db_table = 'boleta'

    def __str__(self):
        return '{}'.format(self.nro_boleta)


class CatProducto(models.Model):
    id_categoria = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cat_producto'

    def __str__(self):
        return self.nombre


class DetalleBoleta(models.Model):
    num_detalle = models.AutoField(primary_key=True)
    nro_boleta = models.ForeignKey('Boleta', models.CASCADE, db_column='nro_boleta', verbose_name='Boleta nro')
    id_producto = models.ForeignKey('Producto', models.CASCADE, db_column='id_producto', verbose_name='Producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField(verbose_name='Precio unitario')

    class Meta:
        managed = False
        db_table = 'detalle_boleta'
        unique_together = (('nro_boleta', 'num_detalle'),)

    @property
    def total_item(self):
        return self.cantidad * self.precio_unit


class DetalleFactura(models.Model):
    num_detalle = models.AutoField(primary_key=True)
    nro_factura = models.ForeignKey('Factura', models.CASCADE, db_column='nro_factura',verbose_name='Factura:')
    id_producto = models.ForeignKey('Producto', models.CASCADE, db_column='id_producto', verbose_name='Producto:')
    cantidad = models.FloatField()
    precio_unit = models.FloatField(verbose_name='Precio unitario')

    class Meta:
        managed = False
        db_table = 'detalle_factura'
        unique_together = (('nro_factura', 'num_detalle'),)

    @property
    def total_item(self):
        return self.cantidad * self.precio_unit


class DetalleOrden(models.Model):
    num_detalle = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey('OrdenCompra', models.CASCADE, db_column='id_orden', verbose_name='Orden')
    id_producto = models.ForeignKey('Producto', models.CASCADE, db_column='id_producto', verbose_name='Producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField(verbose_name='Precio unitario')

    class Meta:
        managed = False
        db_table = 'detalle_orden'
        unique_together = (('id_orden', 'num_detalle'),)

    @property
    def total_item(self):
        return self.cantidad * self.precio_unit


class DetalleVenta(models.Model):
    num_detalle = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey('Venta', models.CASCADE, db_column='id_venta')
    id_producto = models.ForeignKey('Producto', models.CASCADE, db_column='id_producto', verbose_name='Producto')
    cantidad = models.FloatField()
    precio_unit = models.FloatField(verbose_name='Precio unitario')

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('num_detalle', 'id_venta'),)

    @property
    def total_item(self):
        return self.cantidad * self.precio_unit


class EstadoOrden(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_orden'

    def __str__(self):
        return self.descripcion


class EstadoVenta(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_venta'

    def __str__(self):
        return self.descripcion


class Factura(models.Model):
    nro_factura = models.BigAutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    razon_soc = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    contacto = models.IntegerField()
    estado = models.BooleanField(default=True, verbose_name='Desmarque esta casilla para anular la factura')
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'factura'

    def __str__(self):
        return 'Factura N°: {} / fecha: {}'.format(self.nro_factura, self.fecha)


class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', verbose_name='Usuario')
    id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='id_estado', default=1)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', verbose_name='Proveedor')

    class Meta:
        managed = False
        db_table = 'orden_compra'

    def __str__(self):
        return '{}'.format(self.id_orden)


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio_unit = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    marca = models.CharField(max_length=50)
    fecha_venc = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(CatProducto, models.DO_NOTHING, db_column='id_categoria', verbose_name='Categoría')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', verbose_name='Proveedor')
    url_img = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class ProductoTemp(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    descripcion = models.CharField(max_length=500)
    precio_unit = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    marca = models.CharField(max_length=50)
    fecha_venc = models.DateField(blank=True, null=True)
    id_categoria = models.ForeignKey(CatProducto, models.DO_NOTHING, db_column='id_categoria', verbose_name='Categoría')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', verbose_name='Proveedor')
    url_img = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_temp'


class Proveedor(models.Model):
    id_proveedor = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(unique=True, max_length=10)
    telefono = models.FloatField()
    rubro = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'

    def __str__(self):
        return self.nombre


class Recepcion(models.Model):
    id_recepcion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_orden = models.ForeignKey(OrdenCompra, models.CASCADE, db_column='id_orden')

    class Meta:
        managed = False
        db_table = 'recepcion'
        unique_together = (('id_recepcion', 'id_orden'),)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, rut, nombre, apellido, telefono, direccion, comuna, password=None):
        if not email:
            raise ValueError('El usuario debe registrar un email')
        if not rut:
            raise ValueError('El usuario debe registrar su rut')
        if not nombre:
            raise ValueError('El usuario debe registrar su nombre')
        if not apellido:
            raise ValueError('El usuario debe registrar su apellido')
        if not telefono:
            raise ValueError('El usuario debe registrar su telefono')
        if not direccion:
            raise ValueError('El usuario debe registrar su direccion')
        if not comuna:
            raise ValueError('El usuario debe registrar su comuna')

        user = self.model(
            email=self.normalize_email(email),
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            direccion=direccion,
            comuna=comuna
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, rut, nombre, apellido, telefono, direccion, comuna, password):
        user = self.create_user(
            email=email,
            rut=rut,
            password=password,
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            direccion=direccion,
            comuna=comuna,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=500, verbose_name='Contraseña')
    rut = models.CharField(unique=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.CharField(unique=True, max_length=150, verbose_name='Email')
    telefono = models.FloatField(max_length=9, verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    comuna = models.CharField(max_length=30, verbose_name='Comuna')
    cargo = models.CharField(max_length=50, blank=True, null=True)
    rubro = models.CharField(max_length=100, blank=True, null=True)
    esempresa = models.BooleanField(default=False, verbose_name='Marque esta casilla si es una empresa')
    es_proveedor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('rut', 'email'),)
        permissions = [
            ("editar_orden", "Puede editar las ordenes de compra"),
            ("ver_ordenes", "Puede ver las ordenes de compra"),
        ]

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido',
                       'telefono', 'direccion', 'comuna']

    objects = MyAccountManager()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField(default=timezone.now)
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado', default=1)
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', verbose_name='Cliente')

    class Meta:
        managed = False
        db_table = 'venta'

    def __str__(self):
        return '{}'.format(self.id_venta)
