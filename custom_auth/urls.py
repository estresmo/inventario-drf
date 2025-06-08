from django.urls import path
from .views import UsuarioCreate

urlpatterns = [
    path("registro/", UsuarioCreate.as_view(), name="registro"),
]