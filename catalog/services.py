from config.settings import CACHES
from catalog.models import Product, Category
from django.core.cache import cache
from django.shortcuts import get_object_or_404

def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст получает данные из БД"""
    if not CACHES:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_products_by_category(category_id):
    category = get_object_or_404(Category, id=category_id)
    return Product.objects.filter(category=category)
