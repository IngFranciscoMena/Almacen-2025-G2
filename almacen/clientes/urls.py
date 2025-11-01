from django.urls import path
from .views import pagina_home

urlpatterns = [
    path('home/', pagina_home, name='home'),
]