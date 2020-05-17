from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from compras.models import Compra
from compras.serializers import CompraSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CompraPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'compras.change_compra',
                    'partial_update': 'compras.change_compra',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        compra = serializer.save()
        user = self.request.user
        assign_perm('compras.change_compra', user, compra)
        assign_perm('compras.view_compra', user, compra)
        return Response(serializer.data)
