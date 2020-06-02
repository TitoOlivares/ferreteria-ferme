from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserForm
from .models import Producto, CatProducto, Usuario


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


class Register(CreateView):
    model = Usuario
    form_class = CustomUserForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('home')
