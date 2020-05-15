from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from listas.models import Lista
from listas.serializers import ListaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ListaPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'listas.change_lista',
                    'partial_update': 'listas.change_lista',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        lista = serializer.save()
        user = self.request.user
        assign_perm('listas.change_usuario', user, lista)
        assign_perm('listas.view_usuario', user, lista)
        return Response(serializer.data)
