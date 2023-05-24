from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # # Удаление всех записей из таблицы Category
        Category.objects.all().delete()

        # Заполнение таблицы новыми данными из списка
        category_data = [
            {'name': 'Молочные продукты', 'description': 'Продукты, созданные на основе молока'},
            {'name': 'Мясные продукты', 'description': 'Продукты, приготовленные из мяса'},
            {'name': 'Хлебобулочные изделия', 'description': 'Продукт, получаемый методом выпекания из теста'},
            {'name': 'Рыбные продукты', 'description': 'Продукты, связанные с рыбой'},
            {'name': 'Крупы', 'description': 'Зерна различных культур, преимущественно злаковых'},
            {'name': 'Бобовые', 'description': 'Продукты, производимые из различных видов бобов'}
        ]

        for item in category_data:
            Category.objects.create(**item)

        #
