from django.contrib import admin
from .models import TipoUsuario, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)