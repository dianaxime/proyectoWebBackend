from rest_framework import serializers

from facturas.models import Factura
from clientes.serializers import ClienteSerializer
from tiendas.serializers import TiendaSerializer

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = (
            'id',
            'fechaFactura',
            'subtotalFactura',
            'ivaFactura',
            'totalFactura',
            'idCliente',
            'idTienda'
        )