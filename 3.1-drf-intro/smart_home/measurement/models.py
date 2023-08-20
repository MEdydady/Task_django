from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name="measurements"
    )
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"sensor: {self.sensor} temp: {self.temperature} time: {self.created_at}"
