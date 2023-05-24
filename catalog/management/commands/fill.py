from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Удаление всех записей из таблицы Category
        Category.objects.all().delete()

        # Заполнение таблицы новыми данными из списка
        category_data = [
            {'id': 1, 'name': 'Молочные продукты', 'description': 'Продукты, созданные на основе молока'},
            {'id': 2, 'name': 'Мясные продукты', 'description': 'Продукты, приготовленные из мяса'},
            {'id': 3, 'name': 'Хлебобулочные изделия', 'description': 'Продукт, получаемый методом выпекания из теста'},
            {'id': 4, 'name': 'Рыбные продукты', 'description': 'Продукты, связанные с рыбой'},
            {'id': 5, 'name': 'Крупы', 'description': 'Зерна различных культур, преимущественно злаковых'},
            {'id': 6, 'name': 'Бобовые', 'description': 'Продукты, производимые из различных видов бобов'}
        ]

        for item in category_data:
            Category.objects.create(**item)
