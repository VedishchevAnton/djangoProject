from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalog.models import Category, Product


# def category(request):
#     category_list = Category.objects.all()
#     context = {
#         'objects_list': category_list,
#         'title': 'Список категорий продуктов'
#     }
#     return render(request, 'catalog/category_list.html', context)

class CategoryListView(generic.ListView):
    model = Category
    extra_context = {
        'title': 'Список категорий продуктов'
    }


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'objects_list'
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Список продуктов'}

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            product.description = product.description[:100]
        return queryset


def contact(request):
    # Если метод запроса POST, значит пользователь отправил сообщение через форму контактов
    if request.method == 'POST':
        # Получаем данные из формы контактов (имя, email и сообщение)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}\nEmail: {email}\nMessage: {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html', context)


# def products(request):
#     product_list = Product.objects.all()
#     modified_product_list = []
#     for product in product_list:
#         modified_product = product
#         modified_product.description = product.description[:100]
#         modified_product_list.append(modified_product)
#     context = {
#         'objects_list': modified_product_list,
#         'title': 'Список продуктов'
#     }
#     return render(request, 'catalog/product.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'catalog/product_details.html', {'product': product})
