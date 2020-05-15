from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from tiendas.models import Tienda
from tiendas.serializers import TiendaSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='TiendaPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'tiendas.change_tienda',
                    'partial_update': 'tiendas.change_tienda',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        tienda = serializer.save()
        user = self.request.user
        assign_perm('tiendas.change_tienda', user, tienda)
        assign_perm('tiendas.view_tienda', user, tienda)
        return Response(serializer.data)
