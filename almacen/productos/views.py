from django.shortcuts import render
from django.views.generic import ListView
from .models import Categoria

# Create your views here.

# crear vistas genericas para categoria
class CategoriaListView(ListView):

    # indicar cual es el modelo base
    model = Categoria
    fields = ["nombre", "descripcion"]
    template_name = "categorias/categoria-list.html"
    context_object_name = "categorias"