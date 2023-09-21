from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя датчика')
    description = models.TextField(max_length=500,
                                   verbose_name='Описание датчика')

    class Meta:
        ordering = ['id']
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    value = models.FloatField(null=False, blank=False,
                              verbose_name='Температура')
    data_measure = models.DateTimeField(auto_now=True,
                                        verbose_name='Дата и время измерения')

    class Meta:
        ordering = ['data_measure']
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'Датчик {self.sensor} - {self.value} гр.С от {self.data_measure}'
