from django.contrib import admin
from .models import Carro


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "ano", "placa", "valor_diaria", "disponivel")
    list_filter = ("disponivel", "ano")
    search_fields = ("marca", "modelo", "placa")
