from django.urls import path

from .views import ClienteCreateView, ClienteListView

app_name = "clientes"

urlpatterns = [
    path("", ClienteListView.as_view(), name="lista"),
    path("novo/", ClienteCreateView.as_view(), name="criar"),
]
