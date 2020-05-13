from rest_framework import serializers

from listas.models import Lista
from productos.serializers import ProductoSerializer
from empleados.serializers import EmpleadoSerializer

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = (
            'id',
            'fechaLista',
            'cantidadLista',
            'turnoLista',
            'idProducto',
            'idEncargado'
        )