from rest_framework import serializers

from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Usuario
        fields = (
            'id',
            'email',
            'username',
            'tipo',
            'password',
            'password2'
        )
        extra_kwargs = {
				'password': {'write_only': True},
		}	

    def save(self):
        usuario = Usuario(
            email=self.validated_data['email'], username=self.validated_data['username'], tipo=self.validated_data['tipo'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Las contraseñas deben coincidir.'})
        usuario.set_password(password)
        usuario.save()
        return usuario
