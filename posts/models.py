from django.db import models
from django.urls import reverse
# Create your models here.
class Informacion(models.Model):
    text = models.TextField(default = "")
    descripcion = models.TextField(default = "")
    infromacion = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]
        

class Post(models.Model):
    text = models.CharField(max_length=200)
    informacion =models.ForeignKey(
        Informacion,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    autor = models.TextField(default = "")
    def __str__(self):
        return self.text[:500]

    def get_absolute_url(self):
        return reverse('informacion', args=[str(self.id)])