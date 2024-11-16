from rest_framework import viewsets
from .serializers import UsuariosSerializer
from .models import Usuarios

# Create your views here. Funciones que responder al cliente POST, GET, PUT
class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()