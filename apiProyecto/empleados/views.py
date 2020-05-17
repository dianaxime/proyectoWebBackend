from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EmpleadoPermission',
            permission_configuration={
                'base': {
                    'create': True,
                },
                'instance': {
                    # 'retrieve': 'empleados.change_empleado',
                    # 'partial_update': 'empleados.change_empleado',
                    'retrieve': evaluar,
                    'partial_update': evaluar,
                    'modificar_empleado': evaluar,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        empleado = serializer.save()
        user = self.request.user
        assign_perm('empleados.change_empleado', user, empleado)
        assign_perm('empleados.view_empleado', user, empleado)
        return Response(serializer.data)
    
    @action(detail=True, url_path='modificar-empleado', methods=['patch'])
    def modificar_empleado(self, request, pk=None):
        empleado = self.get_object()
        empleado.direccionEmpleado = request.data.get('direccion')
        empleado.telefonoEmpleado = request.data.get('telefono')
        empleado.puestoEmpleado = request.data.get('puesto')
        empleado.save()
        return Response(EmpleadoSerializer(empleado).data)

