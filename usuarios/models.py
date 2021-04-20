from django.db import models
from django.contrib.auth.models import AbstractUser


#modelo para los campos que se usuaran para un usuario personalizado
class UsuarioPers(AbstractUser):
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(default="", max_length=10)
    correo = models.ImageField(default="", null=True, blank=True)
    def __str__(self):
        return self.email