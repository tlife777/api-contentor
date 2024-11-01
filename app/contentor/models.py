from django.db import models


class SensorData(models.Model):
    created_at = (models.DateTimeField(auto_now=True))
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    bateria = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Dado do Sensor"
        verbose_name_plural = "Dados do Sensor"
