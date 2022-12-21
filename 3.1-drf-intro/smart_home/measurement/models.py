from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    measure_date = models.DateField(auto_now=True)
