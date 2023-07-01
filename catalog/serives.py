from django.conf import settings
from django.core.cache import cache
from catalog.models import Category


def get_categories():
    categories = cache.get('categories')
    if categories is None:
        categories = Category.objects.all()
        cache.set('categories', categories)
    return categories


def get_cached_product_data(product):
    if settings.CACHE_ENABLE:
        cache_key = f'product_{product.pk}'
        # Получаем закешированные данные
        cached_data = cache.get(cache_key)
        # Если закешированных данных нет, то создаем их и кешируем
        if cached_data is None:
            cached_data = {
                'description': product.description,  # Описание продукта
                'price': product.price,  # Цена продукта
            }
            cache.set(cache_key, cached_data, 300)  # Кешируем данные на 5 минут
        return cached_data
    else:
        return {
            'description': product.description,  # Описание продукта
            'price': product.price,  # Цена продукта
        }
