from django.contrib import admin
from .models import Locacao


@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "carro",
        "data_retirada",
        "data_devolucao",
        "valor_total",
        "alugado",
    )
    list_filter = ("alugado", "data_retirada", "data_devolucao")
    search_fields = ("cliente__nome", "carro__marca", "carro__modelo", "carro__placa")
