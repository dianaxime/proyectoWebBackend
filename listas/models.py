from django.db import models

# Create your models here.
class Lista(models.Model):
    fechaLista = models.DateField()
    cantidadLista = models.IntegerField(null = False, blank = False)
    turnoLista = models.CharField(max_length = 30)
    idProducto = models.ForeignKey(
        'productos.Producto',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )
    idEncargado = models.ForeignKey(
        'empleados.Empleado',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return str(self.totalFactura)