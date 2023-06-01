from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactCreateView, ProductsListView, ProductsDetailView, ProductsCreatView, \
    ProductsUpdateView, ProductsDeleteView, BlogsListView, BlogsDetailView, BlogCreateView, BlogUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product_details/<int:pk>/', ProductsDetailView.as_view(), name='product_details'),
    path('products/create/', ProductsCreatView.as_view(), name='products_create'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', ProductsDeleteView.as_view(), name='products_delete'),
    path('blogs/', BlogsListView.as_view(), name='blogs'),
    path('blog_details/<int:pk>/', BlogsDetailView.as_view(), name='blog_details'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='blogs_update'),
]
