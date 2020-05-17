from django.db import models

# Create your models here.
class Pedido(models.Model):
    fechaPedido = models.DateTimeField(auto_now = True)
    estadoPedido = models.CharField(max_length = 30, null = False, blank = False)
    pagoPedido = models.CharField(max_length = 30, null = False, blank = False)
    entregaPedido = models.CharField(max_length = 30, null = False, blank = False)
    recogerPedido = models.CharField(max_length = 30, null = False, blank = False)
    idCompras = models.ForeignKey(
        'compras.Compra',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    idFactura = models.ForeignKey(
        'facturas.Factura',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    idEmpleado = models.ForeignKey(
        'empleados.Empleado',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    idCliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.estadoPedido