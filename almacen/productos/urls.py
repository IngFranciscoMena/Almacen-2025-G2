from django.urls import path
# importando las vistas
from .views import (
    CategoriaListView,
    CategoriaCreateView
)

# agregar un identificador de enrutamiento
app_name = "productos"

# enrutamiento
urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name="categoria-list"),
    path('categorias/nueva', CategoriaCreateView.as_view(), name="categoria-create"),
]
