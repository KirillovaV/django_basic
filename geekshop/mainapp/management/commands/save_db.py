import json
from os import path

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/json'


def save_json(file_name, data):
    with open(path.join(JSON_PATH, file_name + '.json'), 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=2)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = ProductCategory.objects.all()
        data = []
        for category in categories:
            data.append({'id': category.id,
                         'name': category.name,
                         'description': category.description,
                         'is_active': category.is_active})

        save_json('categories', data)

        products = Product.objects.all()
        data = []
        for product in products:
            data.append({'id': product.id,
                         'category': product.category.id,
                         'name': product.name,
                         'image': str(product.image),
                         'short_desc': product.short_desc,
                         'description': product.description,
                         'price': float(product.price),
                         'quantity': product.quantity,
                         'is_active': product.is_active})

            save_json('products', data)
