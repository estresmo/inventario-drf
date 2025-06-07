from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductoList, ProductoDetail, CategoriaList, CategoriaDetail

urlpatterns = [
    path("", ProductoList.as_view(), name="productos"),
    path("<int:pk>/", ProductoDetail.as_view(), name="productos-detail"),
    path("categorias/", CategoriaList.as_view(), name="categorias"),
    path("categorias/<int:pk>/", CategoriaDetail.as_view(), name="categorias-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
