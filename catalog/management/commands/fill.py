from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удаление всех записей из таблицы Category
        Category.objects.all().delete()

        # Заполнение таблицы новыми данными из списка
        category_data = [
            {'id': 1, 'name': 'Молочные продукты'},
            {'id': 2, 'name': 'Мясные продукты'},
            {'id': 3, 'name': 'Хлебобулочные изделия'},
            {'id': 4, 'name': 'Рыбные продукты'},
            {'id': 5, 'name': 'Крупы'},
            {'id': 6, 'name': 'Бобовые'}
        ]

        for item in category_data:
            Category.objects.create(**item)
