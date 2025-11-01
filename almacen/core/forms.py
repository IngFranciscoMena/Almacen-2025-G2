# core/forms.py
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(label="Correo electrónico", required=True)
    
    direccion = forms.CharField(label="Dirección", required=False)
    edad = forms.IntegerField(label="Edad", required=False, min_value=0)
    telefono = forms.CharField(label="Teléfono", required=False)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'password1', 'password2', 'direccion', 'edad', 'telefono'
        ]

    # sobreescribir el metodo save del formulario
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            # 🔹 Crear o recuperar el perfil (sin duplicar)
            perfil, created = Perfil.objects.get_or_create(user=user)

            # 🔹 Actualizar datos adicionales
            perfil.direccion = self.cleaned_data.get('direccion')
            perfil.edad = self.cleaned_data.get('edad')
            perfil.telefono = self.cleaned_data.get('telefono')
            perfil.save()

            # 🔹 Asignar grupo "Clientes" automáticamente
            grupo_clientes = Group.objects.filter(name="Clientes").first()
            if grupo_clientes:
                user.groups.add(grupo_clientes)

        return user

