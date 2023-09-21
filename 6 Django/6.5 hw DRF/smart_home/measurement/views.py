# TODO: опишите необходимые обработчики, 
# TODO: рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, \
    MeasurementSerializer, SensorMesurementSerializer


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def test(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        print(sensors)
        for row in sensors:
            print(row.id)
            print(row.name)
            print(row.description)
            print(row.measurement.all())
        ser = SensorSerializer(sensors, many=True)
        data1 = {'message': f'тест пройден'}
        print(data1)
    return Response(ser.data)

@api_view(['POST', 'DELETE'])
def get_measurements(request, pk):
    if request.method == 'POST':
        measurement = Measurement(sensor_id=pk, value=22.3)
        measurement.save()
        data = {'message': f'Измерение: {measurement} успешно создано'}
        return Response(data)
    elif request.method == 'DELETE':
        measurement = Measurement.objects.filter(id=pk)
        info = measurement[0]
        measurement.delete()
        data = {'message': f'Измерение {pk} - {info} успешно удалено'}

    return Response(data)

@api_view(['GET'])
def measurements(request):
    if request.method == 'GET':
        measurements = Measurement.objects.all()
        ser = MeasurementSerializer(measurements, many=True)
        return Response(ser.data)
    else:
        pass


@api_view(['GET', 'POST'])
def sensors(request):

    if request.method == 'GET':
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)
    elif request.method == 'POST':
        sensor = Sensor(name='name1', description='description1')
        sensor.save()
        data = {'message': f'Датчик: {sensor} успешно создан'}
        return Response(data)


@api_view(['GET', 'PATCH', 'DELETE'])
def get_sensors(request, pk):

    if request.method == 'GET':
        sensors = Sensor.objects.filter(id=pk)
        ser = SensorMesurementSerializer(sensors, many=True)
        info = sensors[0]
        print(f'Информация по датчику {pk} - {info} получена')
        return Response(ser.data)

    elif request.method == 'PATCH':
        sensor = Sensor.objects.filter(id=pk).update(
            description = 'Новое описание')
        data = {'message': f'Сенсор {pk} успешно изменен'}
        return Response(data)

    elif request.method == 'DELETE':
        sensor = Sensor.objects.filter(id=pk)
        info = sensor[0]
        sensor.delete()
        data = {'message': f'Датчик {info} успешно удален'}
        return Response(data)
