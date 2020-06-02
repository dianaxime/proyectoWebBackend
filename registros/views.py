from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from registros.models import Registro
from registros.serializers import RegistroSerializer

def evaluar(user, obj, request):
    return user.id == obj.idPedido.idCliente.idUsuario

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='RegistroPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': 'registros.view_registro',
                    'partial_update': 'registros.change_registro',
                }
            }
        ),
    )

    def perform_create(self, serializer):
        registro = serializer.save()
        user = self.request.user
        assign_perm('registros.change_registro', user, registro)
        assign_perm('registros.view_registro', user, registro)
        user.save()
        return Response(serializer.data)