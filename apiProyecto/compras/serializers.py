from rest_framework import serializers

from compras.models import Compra
from productos.serializers import ProductoSerializer
from clientes.serializers import ClienteSerializer

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = (
            'id',
            'cantidadCompra',
            'fechaCompra',
            'estadoCompra',
            'subtotalCompra',
            'idProducto',
            'idCliente'
        )