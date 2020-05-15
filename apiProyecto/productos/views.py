from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from productos.models import Producto
from productos.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ProductoPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'productos.change_producto',
                    'partial_update': 'productos.change_producto',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        producto = serializer.save()
        user = self.request.user
        assign_perm('productos.change_producto', user, producto)
        assign_perm('productos.view_producto', user, producto)
        return Response(serializer.data)
