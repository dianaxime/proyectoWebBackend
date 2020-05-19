from rest_framework import serializers
from datetime import date

from ofertas.models import Oferta
from productos.serializers import ProductoSerializer

class OfertaSerializer(serializers.ModelSerializer):
    vencida = serializers.SerializerMethodField()

    class Meta:
        model = Oferta
        fields = (
            'id',
            'descripcionOferta',
            'descuentoOferta',
            'venceOferta',
            'idProducto',
            'vencida'
        )
    
    def get_vencida(self, obj):
        dia = obj.date
        hoy = date.today()
        resultado = (dia - hoy).days
        return r < 0