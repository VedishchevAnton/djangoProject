from django.contrib import admin
from catalog.models import Category, Product, Contacts, Blogs, Version


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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')
    list_filter = ('product__name', 'is_current')
