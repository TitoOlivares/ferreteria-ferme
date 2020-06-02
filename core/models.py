# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Boleta(models.Model):
    nro_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'boleta'

    def __str__(self):
        return 'Boleta nro: {}'.format(self.nro_boleta)


class CatProducto(models.Model):
    id_categoria = models.SmallAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cat_producto'
        verbose_name = 'categoria de producto'
        verbose_name_plural = 'Categorias de productos'

    def __str__(self):
        return self.nombre


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
        verbose_name = 'detalle de boleta'
        verbose_name_plural = 'Detalles de boletas'

    def __str__(self):
        return 'Detalle boleta nro {}'.format(self.nro_boleta)


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
        verbose_name = 'detalle de factura'
        verbose_name_plural = 'Detalles de facturas'

    def __str__(self):
        return 'Detalle factura nro {}'.format(self.nro_factura)


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
        verbose_name = 'detalle de orden de compra'
        verbose_name_plural = 'Detalles de ordenes de compra'

    def __str__(self):
        return 'Detalle orden nro {}'.format(self.id_orden)


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
        verbose_name = 'detalle de venta'
        verbose_name_plural = 'Detalles de ventas'

    def __str__(self):
        return 'Detalle venta nro {}'.format(self.id_venta)


class EstadoOrden(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_orden'
        verbose_name = 'estado de orden'
        verbose_name_plural = 'Estados de ordenes de compra'

    def __str__(self):
        return self.descripcion


class EstadoVenta(models.Model):
    id_estado = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'estado_venta'
        verbose_name = 'estado de venta'
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
    estado = models.FloatField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'factura'

    def __str__(self):
        return '{}'.format(self.nro_factura)


class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_estado = models.ForeignKey(EstadoOrden, models.DO_NOTHING, db_column='id_estado')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'orden_compra'
        verbose_name = 'orden de compra'
        verbose_name_plural = 'Ordenes de compra'

    def __str__(self):
        return '{}'.format(self.id_orden)


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
    url_img = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre


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
        verbose_name_plural = 'Proveedores'

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
        unique_together = (('id_recepcion', 'id_orden'),)
        verbose_name_plural = 'Recepciones'

    def __str__(self):
        return 'Recepcion nro: {}'.format(self.id_recepcion)


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
    esempresa = models.BooleanField(default=False, verbose_name='Marque esta casilla si es una empresa')
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido',
                       'telefono', 'direccion', 'comuna']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'venta'

    def __str__(self):
        return '{}'.format(self.id_venta)
