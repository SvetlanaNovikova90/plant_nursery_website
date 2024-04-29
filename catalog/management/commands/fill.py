import json

from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json', encoding="UTF-16") as file:
            data = json.load(file)
        return [item for item in data if item['model'] == 'catalog.category']

    @staticmethod
    def json_read_products():
        with open('data.json', encoding="UTF-16") as file:
            data = json.load(file)
        return [item for item in data if item['model'] == 'catalog.product']

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'],
                         name=product['fields']['name'],
                         description=product['fields']['description'],
                         image_ph=product['fields']['image_ph'],
                         category=Category.objects.get(pk=product["fields"]["category"]),
                         price=product['fields']['price'],
                         created_at=product['fields']['created_at'],
                         updated_at=product['fields']['updated_at'])
                         )
        Product.objects.bulk_create(product_for_create)
