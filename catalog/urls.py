from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, contact, ProductsListView, ProductsDetailView, ProductsCreatView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contact/', contact, name='contact'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product_details/<int:pk>/', ProductsDetailView.as_view(), name='product_details'),
    path('products/create/', ProductsCreatView.as_view(), name='products_create'),
]
