from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "login.html")


def registro(request):
    return render(request, "registro.html")


def clientes(request):
    return render(request, "clientes.html")


def productos(request):
    return render(request, "productos.html")


def inventario(request):
    return render(request, "inventario.html")


def inicio(request):
    return render(request, "inicio.html")
