from django.core.cache import cache

from catalog.models import Product
from config import settings


def get_cached_subjects_for_product(category_pk):
    if settings.CACHE_ENABLED:
        key = f'product_list_{category_pk}'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.filter(category_id=category_pk)
            cache.set(key, product_list)
    else:
        product_list = Product.objects.filter(category_id=category_pk)
    return product_list
