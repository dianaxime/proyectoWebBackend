from rest_framework import serializers

from tiendas.models import Tienda

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = (
            'id',
            'nombreTienda',
            'ubicacionTienda',
            'telefonoTienda',
            'faxTienda'
        )