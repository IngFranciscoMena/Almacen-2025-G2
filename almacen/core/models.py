from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username