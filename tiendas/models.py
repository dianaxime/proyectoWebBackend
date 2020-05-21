from django.db import models

# Create your models here.
class Tienda(models.Model):
    nombreTienda = models.CharField(max_length = 40, null = False, blank = False)
    ubicacionTienda = models.CharField(max_length = 100, null = False, blank = False)
    telefonoTienda = models.CharField(max_length = 10, null = False, blank = False)
    faxTienda = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombreTienda