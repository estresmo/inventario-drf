from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductoSerializer, CategoriaSerializer
from .models import Producto, Categoria
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]