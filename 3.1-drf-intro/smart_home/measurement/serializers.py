from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'measure_date', ]


class SensorSerializer(serializers.ModelSerializer):
    measures = MeasuresSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measures', ]


class SensorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'measure_date', 'image']
