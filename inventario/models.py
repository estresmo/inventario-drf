from django.db import models
from productos.models import Producto


# Create your models here.
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()
    observaciones = models.CharField(max_length=200, blank=True)
