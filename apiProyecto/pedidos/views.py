from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='PedidoPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'pedidos.change_pedido',
                    'partial_update': 'pedidos.change_pedido',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        pedido = serializer.save()
        user = self.request.user
        assign_perm('pedidos.change_pedido', user, pedido)
        assign_perm('pedidos.view_pedido', user, pedido)
        return Response(serializer.data)
