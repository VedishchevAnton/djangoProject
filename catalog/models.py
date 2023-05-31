from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=255)  # наименование категории
    description = models.TextField()  # писание категории

    def __str__(self):
        # Метод для отображения объектов класса Category
        # return f'{self.id}: {self.name}'
        return f'{self.name}'

    class Meta:
        verbose_name = "Category"  # наименование модели в единственном числе
        verbose_name_plural = "Categories"  # множественное число наименования модели
        ordering = ('name',)  # сортировка по имени категории


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
    updated_at = models.DateTimeField(auto_now=True)  # дата последнего изменения продукта, с автоматическим

    # обновлением при изменении записи

    def __str__(self):
        return f'{self.image}\n{self.name} {self.description}'

    class Meta:
        verbose_name = "Product"  # наименование модели в единственном числе
        verbose_name_plural = "Products"  # множественное число наименования модели
        ordering = ('-date_of_creation',)  # сортировки по убыванию даты создания продукта


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="user__name")
    email = models.CharField(max_length=100, verbose_name="user_email")
    message = models.CharField(max_length=100, verbose_name="user_message")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class Blogs(models.Model):
    name = models.CharField(max_length=100, verbose_name="blog_name")  # заголовок
    slug = models.CharField(max_length=255)  # slug (реализовать через CharField)
    description = models.TextField(null=True, blank=True, verbose_name="blog_description")  # содержимое
    image = models.ImageField(upload_to='products/', **NULLABLE)  # превью (изображение)
    created_at = models.DateTimeField(default=timezone.now)  # дата создания
    is_published = models.BooleanField(default=True)  # признак публикации
    blog_views = models.IntegerField(verbose_name="blog_views", default=0)  # количество просмотров

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Blog"  # наименование модели в единственном числе
        verbose_name_plural = "Blogs"  # множественное число наименования модели
