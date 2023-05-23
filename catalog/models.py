from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=255)  # наименование категории
    description = models.TextField()  # писание категории

    def __str__(self):
        # Метод для отображения объектов класса Category
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = "Category"  # наименование модели в единственном числе
        verbose_name_plural = "Categories"  # множественное число наименования модели
        ordering = ('name',)  # сортировка по имени категории
        # db_table = "category_table"  # имя таблицы в базе данных для модели


class Product(models.Model):
    name = models.CharField(max_length=255)  # наименование продукта
    description = models.TextField()  # описание продукта
    image = models.ImageField(upload_to='products/', verbose_name='image', **NULLABLE)  # изображение продукта (превью),
    # с указанием пути для
    # сохранения изображений
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # категория продукта, связь с моделью Category
    # через ForeignKey
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена продукта
    date_of_creation = models.DateTimeField(
        default=timezone.now)  # дата создания продукта, с дефолтным значением текущего
    # времени
    last_modified_date = models.DateTimeField(auto_now=True)  # дата последнего изменения продукта, с автоматическим

    # обновлением при изменении записи

    def __str__(self):
        # Метод для отображения объектов класса Product
        return f"{self.name} ({self.category.name}): {self.price}"

    class Meta:
        verbose_name = "Product"  # наименование модели в единственном числе
        verbose_name_plural = "Products"  # множественное число наименования модели
        ordering = ('-date_of_creation',)  # сортировки по убыванию даты создания продукта
        # db_table = "product_table"  # имя таблицы в базе данных для модели
