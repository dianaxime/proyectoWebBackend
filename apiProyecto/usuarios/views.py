from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UsuarioPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    'retrieve': 'usuarios.change_usuario',
                    'partial_update': 'usuarios.change_usuario',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        usuario = serializer.save()
        user = self.request.user
        assign_perm('usuarios.change_usuario', user, usuario)
        assign_perm('usuarios.view_usuario', user, usuario)
        return Response(serializer.data)
