from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Categoria, Proveedor, Producto
# importar reverse_lazy de urls para redireccionar la respuesta a un formulario
from django.urls import reverse_lazy
# importar los formularios personalizados
from .forms import CategoriaForm, ProveedorForm, ProductoForm

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
    form_class = CategoriaForm
    # plantilla donde se va a renderizar el formulario
    template_name = "categorias/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
    
    
# Proveedores
class ProveedorListView(ListView):
    
    model = Proveedor
    fields = ["nombre", "telefono", "contacto"]
    template_name = "proveedores/proveedor-list.html"
    context_object_name = "proveedores"
    
    
class ProveedorCreateView(CreateView):
    
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedores/proveedor-form.html"
    success_url = reverse_lazy("productos:proveedor-list")


# Productos

class ProductoListView(ListView):

    model = Producto
    template_name = "productos/producto-list.html"
    context_object_name = "productos"

class ProductoCreateView(CreateView):

    model = Producto
    form_class = ProductoForm
    template_name = "productos/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")