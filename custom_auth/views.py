from .serializers import UsuarioSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class UsuarioCreate(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
