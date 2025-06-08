from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClienteList, ClienteDetail

urlpatterns = [
    path("", ClienteList.as_view(), name="clientes"),
    path("<int:pk>/", ClienteDetail.as_view(), name="clientes-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
