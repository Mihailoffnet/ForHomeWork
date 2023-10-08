from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer, ProductPositionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# from django.core.paginator import Paginator


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    # pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title',] # DjangoFilterBackend
    search_fields = ['title', 'description',]



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # print(queryset)
    # print(type(queryset))
    # print()
    # for item in queryset:
    #     print(item.positions)
    #     print(type(item.positions))

    # products = ''
    # products = queryset()
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['products',] # DjangoFilterBackend
    # search_fields = ['title', 'description',]