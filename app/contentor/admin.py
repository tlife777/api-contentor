from django.contrib import admin
from contentor.models import SensorData


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de objetos na interface administrativa
    list_display = ("created_at", "latitude", "longitude", "bateria", "volume")

    # Campos que permitirão a filtragem na lateral da interface administrativa
    list_filter = ("created_at",)

    # Campos pelos quais se pode buscar
    search_fields = ("latitude", "longitude")

    # Campos apenas para leitura
    readonly_fields = ("created_at",)
