from rest_framework import serializers
from .models import Product, Stock, StockProduct
from django.core.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    title = ProductSerializer(read_only=True, many=True)
    description = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'title', 'description', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        # print(f'{validated_data=}')
        # print(f'{positions=}')
        for position in positions:
            product = position['product']
            quantity = position['quantity']
            price = position['price']
            StockProduct.objects.create(stock=stock, product=product,
                                        quantity=quantity, price=price).save()

        return stock

    def update(self, instance, validated_data):
        print(f'{validated_data=}')
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        print(f'{positions=}')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        print(f'{stock=}')

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            product = position['product']
            quantity = position['quantity']
            price = position['price']
            # print()
            # print(product)
            # print(product.id)
            # print(StockProduct.objects.filter(stock=stock).values())
            stock_product = StockProduct.objects.filter(stock=stock)
            print(stock_product)
            if product.id in stock_product:
                print('Будем обновлять количество и стоимость товара')

            else:
                StockProduct.objects.update_or_create(
                    stock=stock, product=product, quantity=quantity,
                    price=price)

        return stock
