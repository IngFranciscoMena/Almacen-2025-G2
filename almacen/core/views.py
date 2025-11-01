# importar Vistas Génericas de autenticacion
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistroUsuarioForm

# Create your views here.
class CustomLoginView(LoginView):
    
    template_name = "core/login.html"
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    
    next_page = reverse_lazy("login")


class RegistroUsuarioCreateView(CreateView):
    template_name = 'core/register.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')

    # sobreescribir el metodo form_valid
    def form_valid(self, form):
        # Guardar usuario con el método del formulario
        user = form.save()

        return super().form_valid(form)