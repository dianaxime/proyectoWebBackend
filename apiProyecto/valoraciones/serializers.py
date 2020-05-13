from rest_framework import serializers

from valoraciones.models import Valoracion
from empleados.serializers import EmpleadoSerializer

class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = (
            'id',
            'comentarioValoracion',
            'fechaValoracion',
            'puntuacionValoracion',
            'idEmpleado'
        )