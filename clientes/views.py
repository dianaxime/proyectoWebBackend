from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer
from compras.models import Compra
from compras.serializers import CompraSerializer
from facturas.models import Factura
from facturas.serializers import FacturaSerializer

def evaluar(user, obj, request):
    return user.id == obj.idUsuario.id

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ClientePermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'clientes.view_cliente',
                    # 'partial_update': 'clientes.change_cliente',
                    #'retrieve': evaluar,
                    'partial_update': evaluar,
                    'modificar_cliente': evaluar,
                    'mis_pedidos': evaluar,
                    'mis_compras': evaluar,
                    'mis_facturas': evaluar,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        cliente = serializer.save()
        user = self.request.user
        assign_perm('clientes.change_cliente', user, cliente)
        assign_perm('clientes.view_cliente', user, cliente)
        user.save()
        return Response(serializer.data)

    @action(detail=True, url_path='modificar-cliente', methods=['patch'])
    def modificar_cliente(self, request, pk=None):
        cliente = self.get_object()
        cliente.direccionCliente = request.data.get('direccionCliente')
        cliente.telefonoCliente = request.data.get('telefonoCliente')
        cliente.save()
        return Response(ClienteSerializer(cliente).data)

    @action(detail=True, url_path="mis-pedidos", methods=['get'])
    def mis_pedidos(self, request, pk=None):
        cliente = self.get_object()
        return Response([PedidoSerializer(pedido).data for pedido in Pedido.objects.filter(idCliente=cliente)])

    @action(detail=True, url_path="mis-compras", methods=['get'])
    def mis_compras(self, request, pk=None):
        cliente = self.get_object()
        return Response([CompraSerializer(compra).data for compra in Compra.objects.filter(idCliente=cliente).filter(estadoCompra='activo')])

    @action(detail=True, url_path="mis-facturas", methods=['get'])
    def mis_facturas(self, request, pk=None):
        factura = self.get_object()
        return Response([FacturaSerializer(factura).data for factura in Factura.objects.filter(idCliente=cliente)])