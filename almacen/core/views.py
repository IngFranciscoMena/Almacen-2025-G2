# importar Vistas Génericas de autenticacion
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    
    template_name = "core/login.html"
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    
    next_page = reverse_lazy("login")