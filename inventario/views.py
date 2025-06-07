from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import InventarioSerializer
from .models import Inventario


class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
