from rest_framework import generics
from .models import Filter, SensorData
from .serializers import FilterSerializer, SensorDataSerializer

# Liste et création des filtres
class FilterListCreateView(generics.ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


# Détails d’un filtre spécifique (lecture, mise à jour, suppression)
class FilterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


# Liste et création des données capteurs
class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


# Détails d’une donnée capteur spécifique
class SensorDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
