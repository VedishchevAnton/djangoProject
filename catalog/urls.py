from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, product, product_detail

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
    path('products/', product, name='products'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
