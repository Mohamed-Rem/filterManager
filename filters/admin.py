from django.contrib import admin
from .models import Filter, SensorData

# Affiche les infos de Filter dans l’admin
@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ("filter_id", "brand", "location", "device_id", "install_date", "hours_used")
    search_fields = ("brand", "location", "device_id")
    list_filter = ("brand", "location")

# Affiche les données capteurs dans l’admin
@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ("id", "filter", "timestamp", "temperature", "humidity", "air_quality", "fan_speed")
    list_filter = ("timestamp", "filter")
    search_fields = ("filter__device_id",)
