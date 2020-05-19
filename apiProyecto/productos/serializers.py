from rest_framework import serializers

from productos.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombreProducto',
            'descripcionProducto',
            'precioProducto',
            'descuentoProducto'
        )