from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=200)
    telefonoCliente = models.CharField(max_length=8)
    direccionCliente = models.CharField(max_length=200)
    nitCliente = models.CharField(max_length=15)

    def __str__(self):
        return self.nombreCliente