from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.Serializer):
    # sensor = serializers.CharField()
    value = serializers.FloatField()
    data_measure = serializers.DateTimeField()

    class Meta:
        model = Measurement
        fields = ['sensor', 'value', 'data_measure']

class SensorMesurementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    measurement = MeasurementSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']



