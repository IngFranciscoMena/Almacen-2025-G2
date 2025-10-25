# importar Vistas Génericas de autenticacion
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class CustomLoginView(LoginView):
    
    template_name = "core/login.html"
    redirect_authenticated_user = True
    
