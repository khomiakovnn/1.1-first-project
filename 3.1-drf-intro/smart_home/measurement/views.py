from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasureSerializer, SensorShortSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorShortSerializer

    def post(self, request):
        Sensor(name=request.POST['name'], description=request.POST['description']).save()
        return Response(f"Создан датчик {request.POST['name']}")


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name is not None:
            sensor.name = name
        if description is not None:
            sensor.description = description
        sensor.save()
        return Response(f"Датчик '{sensor.name}' обновлен")


class MeasureView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasureSerializer

    def post(self, request):
        sensor = Sensor.objects.get(id=request.POST.get('sensor'))
        temperature = request.POST.get('temperature')
        image = request.POST.get('image')
        Measurement(sensor=sensor, temperature=temperature, image=image).save()
        return Response(f"Данные датчика '{request.POST['sensor']}' получены")
