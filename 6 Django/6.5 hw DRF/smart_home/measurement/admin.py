from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name',]

@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'data_measure']
    list_filter = ['value',]
