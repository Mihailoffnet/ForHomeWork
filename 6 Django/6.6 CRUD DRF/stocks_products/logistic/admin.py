from django.contrib import admin
from .models import Product, Stock, StockProduct
# from django.core.exceptions import ValidationError
# from django.forms import BaseInlineFormSet

class StockProductInline(admin.TabularInline):
    model = StockProduct
    # formset = StockProductInlineFormset
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['title']
    inlines = [StockProductInline]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    list_filter = ['address']
    inlines = [StockProductInline]

