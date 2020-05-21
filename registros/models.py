from django.db import models

# Create your models here.
class Registro(models.Model):
    cantidadRegistro = models.IntegerField(null = False, blank = False)
    precioUnidadRegistro = models.FloatField(null = False, blank = False)
    subtotalRegistro = models.FloatField(null = False, blank = False)
    descuentoRegistro = models.FloatField(null = False, blank = False)
    totalRegistro = models.FloatField(null = False, blank = False)
    idPedido = models.ForeignKey(
        'pedidos.Pedido',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    idProducto = models.ForeignKey(
        'productos.Producto',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return str(self.subtotalRegistro)