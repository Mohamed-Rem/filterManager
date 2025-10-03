from rest_framework import serializers
from .models import Filter, SensorData

# Serializer pour Filter
class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'  # inclut tous les champs


# Serializer pour SensorData
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
