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
                    # 'retrieve': 'tiendas.change_tienda',
                    # 'partial_update': 'tiendas.change_tienda',
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'modificar_tienda': lambda user, obj, req: user.is_authenticated,
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
    
    @action(detail=True, url_path='modificar-tienda', methods=['patch'])
    def modificar_tienda(self, request, pk=None):
        tienda = self.get_object()
        tienda.ubicacionTienda = request.data.get('direccion')
        tienda.telefonoTienda = request.data.get('telefono')
        tienda.faxTienda = request.data.get('fax')
        tienda.save()
        return Response(TiendaSerializer(tienda).data)
