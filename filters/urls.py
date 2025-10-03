from django.urls import path
from .views import (
    FilterListCreateView, FilterDetailView,
    SensorDataListCreateView, SensorDataDetailView
)

urlpatterns = [
    # Routes pour Filter
    path("filters/", FilterListCreateView.as_view(), name="filters-list"),
    path("filters/<int:pk>/", FilterDetailView.as_view(), name="filters-detail"),

    # Routes pour SensorData
    path("sensor-data/", SensorDataListCreateView.as_view(), name="sensordata-list"),
    path("sensor-data/<int:pk>/", SensorDataDetailView.as_view(), name="sensordata-detail"),
]
