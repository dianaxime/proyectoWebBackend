from django.db import models

# Create your models here.
class Factura(models.Model):
    fechaFactura = models.DateTimeField(auto_now = True)
    subtotalFactura = models.FloatField(null = False, blank = False)
    ivaFactura = models.FloatField(null = False, blank = False)
    totalFactura = models.FloatField(null = False, blank = False)
    idCliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    idTienda = models.ForeignKey(
        'tiendas.Tienda',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return str(self.totalFactura)