from rest_framework import serializers

from pedidos.models import Pedido
from productos.serializers import ProductoSerializer
from empleados.serializers import EmpleadoSerializer
from compras.serializers import CompraSerializer

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            'id',
            'fechaPedido',
            'estadoPedido',
            'pagoPedido',
            'entregaPedido',
            'recogerPedido',
            'idCompras',
            'idProducto',
            'idEmpleado'
        )