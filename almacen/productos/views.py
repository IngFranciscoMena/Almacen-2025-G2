from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Categoria
# importar reverse_lazy de urls para redireccionar la respuesta a un formulario
from django.urls import reverse_lazy

# Create your views here.

# crear vistas genericas para categoria
class CategoriaListView(ListView):

    # indicar cual es el modelo base
    model = Categoria
    fields = ["nombre", "descripcion"]
    template_name = "categorias/categoria-list.html"
    context_object_name = "categorias"
    
    
# crear una vista generica para agregar una categoria
class CategoriaCreateView(CreateView):
    
    # indicar cual es el modelo base
    model = Categoria
    # campos
    fields = ["nombre", "descripcion"]
    # plantilla donde se va a renderizar el formulario
    template_name = "categorias/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
    
    
    