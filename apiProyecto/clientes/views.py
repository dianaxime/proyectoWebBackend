from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

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
                    'partial_update': 'clientes.change_cliente',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        cliente = serializer.save()
        user = self.request.user
        assign_perm('clientes.change_cliente', user, cliente)
        assign_perm('clientes.view_cliente', user, cliente)
        return Response(serializer.data)
