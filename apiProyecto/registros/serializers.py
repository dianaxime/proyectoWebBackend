from rest_framework import serializers

from registros.models import Registro
from productos.serializers import ProductoSerializer
from pedidos.serializers import PedidoSerializer

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = (
            'id',
            'cantidadRegistro',
            'precioUnidadRegistro',
            'subtotalRegistro',
            'descuentoRegistro',
            'totalRegistro',
            'idProducto',
            'idPedido'
        )