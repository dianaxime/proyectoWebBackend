from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length = 200, null = False, blank = False)
    telefonoCliente = models.CharField(max_length = 8, null = False, blank = False)
    direccionCliente = models.CharField(max_length = 200, null = False, blank = False)
    nitCliente = models.CharField(max_length = 15, null = False, blank = False)
    idUsuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete = models.CASCADE,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nombreCliente