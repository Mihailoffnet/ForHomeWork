from django.urls import path
from .views import sensors, measurements, get_sensors, get_measurements, test

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('measurements/<int:pk>/', get_measurements, name='get_measurements'),
    path('measurements/', measurements, name='measurements'),
    path('sensors/', sensors, name='sensors'),
    path('sensors/<int:pk>/', get_sensors, name='get_sensors'),
    path('test/', test, name='test'),

]
