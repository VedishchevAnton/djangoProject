from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, products, product_details

# urlpatterns = [
#     path('', home, name='home'),
#     path('contact/', index),
#     path('contact/', contact)
#     # path('contact/', product_detail, name='product_detail'),
# ]


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('product_details/<int:product_id>/', product_details, name='product_details'),
]
