from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombreEmpleado = models.CharField(max_length = 200, null = False, blank = False)
    telefonoEmpleado = models.CharField(max_length = 8)
    direccionEmpleado = models.CharField(max_length = 200)
    puestoEmpleado = models.CharField(max_length = 15, null = False, blank = False)
    idUsuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nombreEmpleado