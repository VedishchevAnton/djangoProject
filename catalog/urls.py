from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contact, ProductListView, product_details


app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contact/', contact, name='contact'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product_details/<int:product_id>/', product_details, name='product_details'),
]
