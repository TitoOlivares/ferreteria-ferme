from django.contrib import admin
from .models import Usuario, Producto
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'rut')
    search_fields = ('email', 'rut')
    readonly_fields = ('last_login', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    ordering = ('email',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto)
