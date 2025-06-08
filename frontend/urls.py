from django.urls import path
from .views import login, registro, clientes, productos, inventario, inicio, categorias

urlpatterns = [
    path("login/", login, name="login"),
    path("registro/", registro, name="registro"),
    path("clientes/", clientes, name="clientes"),
    path("productos/", productos, name="productos"),
    path("inventario/", inventario, name="inventario"),
    path("categorias/", categorias, name="categorias"),
    path("", inicio, name="inicio"),
]
