from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from ofertas.models import Oferta
from ofertas.serializers import OfertaSerializer

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='OfertaPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'ofertas.change_oferta',
                    'partial_update': 'ofertas.change_oferta',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        oferta = serializer.save()
        user = self.request.user
        assign_perm('ofertas.change_oferta', user, oferta)
        assign_perm('ofertas.view_oferta', user, oferta)
        return Response(serializer.data)
