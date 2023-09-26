# TODO: опишите необходимые обработчики, 
# TODO: рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
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
    

class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class GetSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorMesurementSerializer

    def patch(self, request, pk):
        body = json.loads(request.body)
        if not Sensor.objects.filter(id=pk):
            data = {'message': f'Сенсор {pk} не найден'}
        else:
            sensor = Sensor.objects.filter(id=pk).update(description=body['description'])
            data = {'message': f'Сенсор {pk} успешно изменен'}
        return Response(data)
    
    def delete(self, request, pk):
        sensor = Sensor.objects.filter(id=pk)
        if not sensor:
            data = {'message': f'Датчик {pk} не найден базе'}
        else:
            info = sensor[0]
            sensor.delete()
            data = {'message': f'Датчик {info} успешно удален'}
        return Response(data)

    
class MeasurementsView(generics.ListCreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class GetMeasurementsView(RetrieveAPIView):

    def delete(self, request, pk):
        measurement = Measurement.objects.filter(id=pk)
        if not measurement:
            data = {'message': f'Измерение {pk} не найдено'}
        else:
            info = measurement[0]
            measurement.delete()
            data = {'message': f'Измерение {pk} - {info} успешно удалено'}
        return Response(data)
