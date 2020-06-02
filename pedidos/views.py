from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

from permisos.services import APIPermissionClassFactory
from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer

def evaluar(user, obj, request):
    return user.id == obj.idEmpleado.idUsuario

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='PedidoPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': 'pedidos.view_pedido',
                    #'partial_update': 'pedidos.change_pedido',
                    'confirmado': lambda user, obj, req: user.is_authenticated,
                    'completado': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        pedido = serializer.save()
        user = self.request.user
        assign_perm('pedidos.change_pedido', user, pedido)
        assign_perm('pedidos.view_pedido', user, pedido)
        user.save()
        return Response(serializer.data)

    @action(detail=False, url_path='confirmado', methods=['patch'])
    def entregar(self, request, pk=None):
        cliente = request.data.get('idCliente')
        empleado = request.data.get('idEmpleado')
        pedidos = Pedido.objects.filter(idCliente=cliente).filter(estadoPedido='pendiente')
        pedidosEntregados = []
        for pedido in pedidos:
            pedido.estadoPedido = 'confirmado'
            pedido.idEmpleado = empleado
            pedido.save()
            pedidosEntregados.append(PedidoSerializer(pedido).data)
        return Response(pedidosEntregados) 

    @action(detail=False, url_path='completado', methods=['patch'])
    def cancelar(self, request, pk=None):
        cliente = request.data.get('idCliente')
        pedidos = Pedido.objects.filter(idCliente=cliente).filter(entregaPedido='pendiente')
        pedidosCancelados = []
        for pedido in pedidos:
            pedido.entregaPedido = 'completado'
            pedido.save()
            pedidosCancelados.append(PedidoSerializer(pedido).data)
        return Response(pedidosCancelados) 
