from django.urls import path

from .views import LocacaoCreateView, LocacaoListView

app_name = "locacoes"

urlpatterns = [
    path("", LocacaoListView.as_view(), name="lista"),
    path("nova/", LocacaoCreateView.as_view(), name="nova"),
]
