from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from facturas.models import Factura
from facturas.serializers import FacturaSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='FacturaPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'facturas.change_factura',
                    'partial_update': 'facturas.change_factura',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        factura = serializer.save()
        user = self.request.user
        assign_perm('facturas.change_factura', user, factura)
        assign_perm('facturas.view_factura', user, factura)
        return Response(serializer.data)
