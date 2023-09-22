# TODO: опишите необходимые обработчики, 
# TODO: рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, \
    SensorMesurementSerializer

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def test(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        sensor = Sensor(name=body['name'], description=body['description'])
        sensor.save()
        data = {'message': f'Датчик: {sensor} успешно создан'}
        print(data)
        return Response(data)


class SensorView(ListAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        body = json.loads(request.body)
        sensor = Sensor(name=body['name'], description=body['description'])
        sensor.save()
        data = {'message': f'Датчик: {sensor} успешно создан'}
        return Response(data)
    
class GetSensorView(RetrieveAPIView):

    queryset = Sensor.objects.all()
    serializer_class = SensorMesurementSerializer

    def patch(self, request, pk):
        body = json.loads(request.body)
        sensor = Sensor.objects.filter(id=pk)[0]
        old_description = sensor.description
        new_description = old_description + ' / ' + body['description']
        sensor = Sensor.objects.filter(id=pk).update(description=
                                                     new_description)
        data = {'message': f'Сенсор {pk} успешно изменен'}
        return Response(data)

    def delete(self, request, pk):
        sensor = Sensor.objects.filter(id=pk)
        info = sensor[0]
        sensor.delete()
        data = {'message': f'Датчик {info} успешно удален'}
        return Response(data)
    
class MeasurementsView(ListAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        body = json.loads(request.body)
        measurement = Measurement(sensor_id=body['sensor'], value=
                                  body['temperature'])
        measurement.save()
        data = {'message': f'Измерение: {measurement} успешно создано'}
        return Response(data)

class GetMeasurementsView(RetrieveAPIView):

    def delete(self, request, pk):
        measurement = Measurement.objects.filter(id=pk)
        info = measurement[0]
        measurement.delete()
        data = {'message': f'Измерение {pk} - {info} успешно удалено'}
        return Response(data)
