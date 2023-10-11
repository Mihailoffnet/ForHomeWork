from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['id']

    def __str__(self):
        return f'{self.address}'

class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock, 
        verbose_name='Наличие',
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Товар',
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(
        default=1, 
        verbose_name ='Количество',
    )
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        verbose_name ='Цена',
        validators=[MinValueValidator(0)],
    )
    def __str__(self):
        return f'{self.stock} - {self.product}'