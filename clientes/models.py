from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
