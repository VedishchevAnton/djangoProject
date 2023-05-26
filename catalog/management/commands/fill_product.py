from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_list = [
            {'name': 'Молоко "Простоквашино"',
             'description': 'пастеризованное 2,5% вырабатывается из натурального коровьего молока', 'category_id': 7,
             'price': 67.0},
            {'name': 'Колбаса "Папа Может"', 'description': 'Мясная вареная 500г приготовлена по оригинальной рецептур',
             'category_id': 8, 'price': 320},
            {'name': 'Хлеб "Зарядье"', 'description': 'изготовлен из лучших пшеницы', 'category_id': 9, 'price': 45}
        ]
        category_for_create = []
        for item in products_list:
            category_for_create.append(Product(**item))
        Product.objects.bulk_create(category_for_create)
