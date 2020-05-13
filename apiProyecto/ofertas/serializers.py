from rest_framework import serializers

from ofertas.models import Oferta
from productos.serializers import ProductoSerializer

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = (
            'id',
            'descripcionOferta',
            'descuentoOferta',
            'venceOferta',
            'idProducto'
        )