from django.db import models

# Create your models here.
class Valoracion(models.Model):
    comentarioValoracion = models.CharField(max_length = 100)
    fechaValoracion = models.DateTimeField(auto_now = True)
    puntuacionValoracion = models.IntegerField()
    idEmpleado = models.ForeignKey(
        'empleados.Empleado',
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
        return self.comentarioValoracion