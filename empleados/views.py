from django.shortcuts import render

# Create your views here.
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permisos.services import APIPermissionClassFactory
from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer
from valoraciones.models import Valoracion
from valoraciones.serializers import ValoracionSerializer
from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer
from django.db.models import Avg

def evaluar(user, obj, request):
    return user.id == obj.idUsuario

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
                    'retrieve': 'empleados.change_empleado',
                    # 'partial_update': 'empleados.change_empleado',
                    #'retrieve': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'modificar_empleado': lambda user, obj, req: user.is_authenticated,
                    'mis_comentarios': lambda user, obj, req: user.is_authenticated,
                    'mi_puntuacion': lambda user, obj, req: user.is_authenticated,
                    'mis_pedidos': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        empleado = serializer.save()
        user = self.request.user
        assign_perm('empleados.change_empleado', user, empleado)
        assign_perm('empleados.view_empleado', user, empleado)
        user.save()
        return Response(serializer.data)
    
    @action(detail=True, url_path='modificar-empleado', methods=['patch'])
    def modificar_empleado(self, request, pk=None):
        empleado = self.get_object()
        empleado.direccionEmpleado = request.data.get('direccion')
        empleado.telefonoEmpleado = request.data.get('telefono')
        empleado.save()
        return Response(EmpleadoSerializer(empleado).data)

    @action(detail=True, url_path="mis-comentarios", methods=['get'])
    def mis_comentarios(self, request, pk=None):
        empleado = self.get_object()
        return Response([ValoracionSerializer(valoracion).data for valoracion in Valoracion.objects.filter(idEmpleado=empleado)])

    @action(detail=True, url_path="mi-puntuacion", methods=['get'])
    def mi_puntuacion(self, request, pk=None):
        empleado = self.get_object()
        puntuacion = Valoracion.objects.filter(idEmpleado=empleado).aggregate(Avg('puntuacionValoracion'))
        return Response({'puntuacion': float(puntuacion['puntuacionValoracion__avg'])})
    
    @action(detail=True, url_path="mis-pedidos", methods=['get'])
    def mis_pedidos(self, request, pk=None):
        empleado = self.get_object()
        return Response([PedidoSerializer(pedido).data for pedido in Pedido.objects.filter(idEmpleado=empleado).filter(estadoPedido='pendiente')])

