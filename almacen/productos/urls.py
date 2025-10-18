from django.urls import path
# importando las vistas
from .views import (
    CategoriaListView,
    CategoriaCreateView,
    # proveedores
    ProveedorListView,
    ProveedorCreateView,
    # productos
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView
)

# agregar un identificador de enrutamiento
app_name = "productos"

# enrutamiento
urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name="categoria-list"),
    path('categorias/nueva', CategoriaCreateView.as_view(), name="categoria-create"),
    # proveedores
    path('proveedores/', ProveedorListView.as_view(), name="proveedor-list"),
    path('proveedores/nuevo', ProveedorCreateView.as_view(), name="proveedor-create"),
    # productos
    path('', ProductoListView.as_view(), name="producto-list"),
    path('nuevo/', ProductoCreateView.as_view(), name="producto-create"),    
    path('editar/<int:pk>', ProductoUpdateView.as_view(), name="producto-update"),    
]
