from rest_framework import serializers

from valoraciones.models import Valoracion
from empleados.serializers import EmpleadoSerializer
from clientes.serializers import ClienteSerializer

class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = (
            'id',
            'comentarioValoracion',
            'fechaValoracion',
            'puntuacionValoracion',
            'idEmpleado',
            'idCliente'
        )