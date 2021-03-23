from django.db import models
from django.urls import reverse
#se crea el modelo informacion que es el segundo en donde se obtedra infromacion de lo ingresado
class Informacion(models.Model):
    titulo = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    informacion = models.TextField(default = "")
    def __str__(self):
        return self.titulo[:500]
        
#modelo posts que es el principal y el que obtendra la llave foranea del informacion
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    informacion =models.ForeignKey(
        Informacion,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    precio = models.TextField(default = "")
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('cortes', args=[str(self.id)])