from rest_framework import serializers

from clientes.models import Cliente
from usuarios.serializers import UsuarioSerializer

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nombreCliente',
            'telefonoCliente',
            'direccionCliente',
            'nitCliente',
            'idUsuario'
        )