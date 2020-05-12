from django.db import models

# Create your models here.
class Oferta(models.Model):
    descripcionOferta = models.CharField(max_length = 100, null = False, blank = False)
    descuentoOferta = models.FloatField(null = False, blank = False)
    venceOferta = models.DateTimeField(auto_now = False)
    idProducto = models.ForeignKey(
        'productos.Producto',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nombreTienda