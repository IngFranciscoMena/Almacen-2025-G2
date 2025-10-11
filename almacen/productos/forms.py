# importar formularios de django
from django import forms
# importar los modelos
from .models import Categoria, Proveedor

# crear un formulario personalizado
class CategoriaForm(forms.ModelForm):
    
    # personalizar el formulario
    class Meta:
        model = Categoria
        # campos
        fields = ["nombre", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre Categoria"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción Categoria", "rows": 3})
        }
        
        
class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        # campos
        fields = ["nombre", "telefono", "email", "direccion", "contacto"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre Proveedor"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "Numero Telefono", "type": "tel"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Correo Electronico", "type": "email"}),
            "direccion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Dirección Proveedor", "rows": 3}),
            "contacto": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre Contacto"}),
        }