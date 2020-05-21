from rest_framework import serializers

from empleados.models import Empleado
from usuarios.serializers import UsuarioSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = (
            'id',
            'nombreEmpleado',
            'telefonoEmpleado',
            'direccionEmpleado',
            'puestoEmpleado',
            'idUsuario'
        )