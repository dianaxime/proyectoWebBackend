from django.db import models

# Create your models here.
class Compra(models.Model):
    cantidadCompra = models.IntegerField(null = False, blank = False)
    fechaCompra = models.DateTimeField(auto_now_add = True)
    estadoCompra = models.CharField(max_length = 30, null = False, blank = False)
    subtotalCompra = models.FloatField(null = False, blank = False)
    descuentoCompra = models.FloatField(null = False, blank = False)
    idProducto = models.ForeignKey(
        'productos.Producto',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    idCliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.estadoCompra
