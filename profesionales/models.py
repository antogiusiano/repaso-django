from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()
    tarjeta_presentacion = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=50)
    