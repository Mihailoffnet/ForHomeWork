from django.urls import path


from .views import test, SensorView, MeasurementsView, GetSensorView, \
    GetMeasurementsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('measurements/<int:pk>/', GetMeasurementsView.as_view(), 
         name='get_measurements'),
    path('measurements/', MeasurementsView.as_view(), name='measurements'),
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', GetSensorView.as_view(), name='get_sensors'),
    path('test/', test, name='test'),

]
