from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer

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
                    'retrieve': 'usuarios.view_usuario',
                    'partial_update': 'usuarios.change_usuario',
                    'mi_tipo': 'usuarios.view_usuario',
                    'cliente': 'usuarios.view_usuario',
                    'empleado': 'usuarios.view_usuario',
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

    @action(detail=True, url_path="mi-tipo", methods=['get'])
    def mi_tipo(self, request, pk=None):
        usuario = self.get_object()
        return Response({'tipo': usuario.tipo})

    @action(detail=True, url_path="cliente", methods=['get'])
    def cliente(self, request, pk=None):
        usuario = self.get_object()
        return Response([ClienteSerializer(cliente).data for cliente in Cliente.objects.filter(idUsuario=usuario)])

    @action(detail=True, url_path="empleado", methods=['get'])
    def empleado(self, request, pk=None):
        usuario = self.get_object()
        return Response([EmpleadoSerializer(empleado).data for empleado in Empleado.objects.filter(idUsuario=usuario)])