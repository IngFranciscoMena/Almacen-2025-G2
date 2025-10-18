# importar formularios de django
from django import forms
# importar los modelos
from .models import Categoria, Proveedor, Producto

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

# crear un formulario personalizado para el producto
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["nombre","descripcion","precio_compra","precio_venta","categoria","proveedor","activo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre Producto"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción Producto", "rows": 3}
            ),
            "precio_compra": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "precio_venta": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "categoria": forms.Select(
                attrs={"class":"form-select"}
            ),
            "proveedor": forms.Select(
                attrs={"class":"form-select"}
            ),
            "activo": forms.CheckboxInput(
                attrs={"class": "form-check-input", "placeholder": "Nombre Producto"}
            ),
        }