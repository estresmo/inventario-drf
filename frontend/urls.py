from django.urls import path
from .views import login, registro, clientes, productos, inventario, inicio

urlpatterns = [
    path("login/", login, name="login"),
    path("registro/", registro, name="registro"),
    path("clientes/", clientes, name="clientes"),
    path("productos/", productos, name="productos"),
    path("inventario/", inventario, name="inventario"),
    path("", inicio, name="inicio"),
]
