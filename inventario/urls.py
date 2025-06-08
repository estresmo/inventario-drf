from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InventarioList, InventarioDetail

urlpatterns = [
    path("", InventarioList.as_view(), name="inventario"),
    path("<int:pk>/", InventarioDetail.as_view(), name="inventario-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
