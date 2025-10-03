from django.db import models

# Représente un filtre 
class Filter(models.Model):
    filter_id = models.AutoField(primary_key=True)              # Clé primaire auto-incrémentée
    brand = models.CharField(max_length=50)                     # Nom de la marque du filtre
    install_date = models.DateTimeField()                       # Date d’installation
    hours_used = models.IntegerField(default=0)                 # Nombre d’heures d’utilisation
    location = models.CharField(max_length=50, blank=True)      # Emplacement du filtre
    device_id = models.CharField(max_length=100, unique=True)   # Identifiant de l’ESP32

    def __str__(self):
        return f"{self.brand} - {self.location} (ESP: {self.device_id})"


# Représente les mesures collectées par les capteurs d’un filtre
class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE, related_name="sensor_data")    # Relation One-to-Many : un filtre peut avoir plusieurs donnée
    timestamp = models.DateTimeField(auto_now_add=True)                                         # Ajouté automatiquement lors de la création
    temperature = models.FloatField()                                                           # Température
    humidity = models.FloatField()                                                              # Humidité
    air_quality = models.FloatField(null=True, blank=True)                                      # Qualité de l’air
    fan_speed = models.IntegerField(default=0)                                                  # Vitesse du ventilateur

    def __str__(self):
        return f"Data {self.id} for Filter {self.filter.device_id} at {self.timestamp}"
