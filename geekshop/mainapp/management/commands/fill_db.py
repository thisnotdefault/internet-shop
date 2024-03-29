import json
import os

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory

JSON_PATH = "mainapp/json"


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json"), "r") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json("products")

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product["category"] = category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.create_superuser(
            "admin", "admin@localhost", "adminadmin", age=33
        )
