from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        # fields = ('id', 'usuario', 'correo', 'contraseña')
        fields = '__all__'
