from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from valoraciones.models import Valoracion
from valoraciones.serializers import ValoracionSerializer

class ValoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ValoracionPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'valoraciones.change_valoracion',
                    'partial_update': 'valoraciones.change_valoracion',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        valoracion = serializer.save()
        user = self.request.user
        assign_perm('valoraciones.change_valoracion', user, valoracion)
        assign_perm('valoraciones.view_valoracion', user, valoracion)
        return Response(serializer.data)
