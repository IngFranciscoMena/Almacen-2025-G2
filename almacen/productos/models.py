from django.db import models

# Create your models here.

# modelo categoria
class Categoria(models.Model):

    # atributos
    nombre = models.CharField(max_length=50, unique=True) # nombre varchar(50) unique = true not null
    descripcion = models.TextField(max_length=255, null=True, blank=True) 

    # ajustes a las tablas y modelos => 's o => oes
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

    # polimorfismo
    def __str__(self):
        return f"{self.nombre}"

# modelo proveedor
class Proveedor(models.Model):

    # atributos
    nombre = models.CharField(max_length=50) # nombre varchar(50) unique = true not null
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True) 
    direccion = models.TextField(max_length=255, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)

    # ajustes a las tablas y modelos => 's o => oes
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["nombre"]

    # polimorfismo
    def __str__(self):
        return f"{self.nombre}"

# importar la clase Model de models.
# create table Producto()
class Producto(models.Model): # aplicando herencia
    # (el id Django lo genera de manera automatica)
    # crear los atributos

    nombre = models.CharField(max_length=50) # nombre varchar(50) not null
    descripcion = models.TextField(null=True, max_length=150) # descripcion varchar(150)
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2) # precio decimal(12,2) not null
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)


    # ajustes a las tablas y modelos => 's o => oes
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    # crear un metodo
    def __str__(self): # polimorfismo
        return f"{self.nombre} - {self.stock} unidades"