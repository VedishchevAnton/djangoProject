from django.contrib import admin
from catalog.models import Category, Product, MyImage

# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(MyImage)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
