from django.db import models

# Create your models here.
class Producto(models.Model):
    nombreProducto = models.CharField(max_length = 40, null = False, blank = False)
    descripcionProducto = models.CharField(max_length = 100)
    precioProducto = models.FloatField(null = False, blank = False)

    def __str__(self):
        return self.nombreProducto