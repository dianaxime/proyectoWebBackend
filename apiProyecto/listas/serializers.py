from rest_framework import serializers
from datetime import date

from listas.models import Lista
from productos.serializers import ProductoSerializer
from empleados.serializers import EmpleadoSerializer

class ListaSerializer(serializers.ModelSerializer):
    esHoy = serializers.SerializerMethodField()

    class Meta:
        model = Lista
        fields = (
            'id',
            'fechaLista',
            'cantidadLista',
            'turnoLista',
            'idProducto',
            'idEncargado',
            'esHoy'
        )
    
    def get_esHoy(self, obj):
        dia = obj.fechaLista
        hoy = date.today()
        resultado = (dia - hoy).days
        return resultado == 0