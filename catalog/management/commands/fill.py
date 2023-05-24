from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Заполнение таблицы новыми данными из списка
        category_data = [
            {'name': 'Молочные продукты', 'description': 'Продукты, созданные на основе молока'},
            {'name': 'Мясные продукты', 'description': 'Продукты, приготовленные из мяса'},
            {'name': 'Хлебобулочные изделия', 'description': 'Продукт, получаемый методом выпекания из теста'},
            {'name': 'Рыбные продукты', 'description': 'Продукты, связанные с рыбой'},
            {'name': 'Крупы', 'description': 'Зерна различных культур, преимущественно злаковых'},
            {'name': 'Бобовые', 'description': 'Продукты, производимые из различных видов бобов'}
        ]
        category_for_create = []
        for category in category_data:
            category_for_create.append(Category(**category))
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

