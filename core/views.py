from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UsuarioForm
from .models import Producto, CatProducto, Usuario
from django.contrib.auth import login, authenticate


# Create your views here.

def home(request):
    producto = Producto.objects.all()
    categoria = CatProducto.objects.all()
    data = {
        'productos': producto,
        'categorias': categoria,
    }
    return render(request, 'core/home.html', data)


class registro_usuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'registration/registrar.html'
    success_url = reverse_lazy('login')

