import json

from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json', encoding="UTF-16") as file:
            data = json.load(file)
        return [item for item in data if item['model'] == 'catalog.category']

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )
        Category.objects.bulk_create(category_for_create)
