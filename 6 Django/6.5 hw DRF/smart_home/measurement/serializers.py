from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['value', 'data_measure']

class SensorMesurementSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']



