from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Заполнение таблицы новыми данными из списка
        category_data = [
            {'id': 1, 'name': 'Молочные продукты', 'description': 'Продукты, созданные на основе молока'},
            {'id': 2, 'name': 'Мясные продукты', 'description': 'Продукты, приготовленные из мяса'},
            {'id': 3, 'name': 'Хлебобулочные изделия', 'description': 'Продукт, получаемый методом выпекания из теста'},
            {'id': 4, 'name': 'Рыбные продукты', 'description': 'Продукты, связанные с рыбой'},
            {'id': 5, 'name': 'Крупы', 'description': 'Зерна различных культур, преимущественно злаковых'},
            {'id': 6, 'name': 'Бобовые', 'description': 'Продукты, производимые из различных видов бобов'}
        ]
        category_for_create = []
        for category in category_data:
            category_for_create.append(Category(**category))
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

