from django.contrib import admin
from catalog.models import Category, Product, Contacts, Blogs


# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email",)


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at", "blog_views")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("created_at",)
