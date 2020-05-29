from django.shortcuts import render
from .models import Producto, CatProducto


# Create your views here.

def home(request):
    producto = Producto.objects.all()
    categoria = CatProducto.objects.all()
    data = {
        'productos': producto,
        'categorias': categoria,
    }
    return render(request, 'core/home.html', data)


def login(request):
    return render(request, 'core/login.html')


def register(request):
    return render(request, 'core/register.html')

