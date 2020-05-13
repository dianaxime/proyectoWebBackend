from rest_framework import serializers

from compras.models import Compra
from productos.serializers import ProductoSerializer

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = (
            'id',
            'cantidadCompra',
            'fechaCompra',
            'estadoCompra',
            'subtotalCompra',
            'idProducto'
        )