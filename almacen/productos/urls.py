from django.urls import path
# importando las vistas
from .views import (
    CategoriaListView
)

# agregar un identificador de enrutamiento
app_name = "productos"

# enrutamiento
urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name="categoria-list")
]
