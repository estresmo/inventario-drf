from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClienteSerializer
from .models import Cliente
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
