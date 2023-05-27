from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product


# def home(request):
#     return render(request, 'catalog/home.html')


def index(request):
    category_list = Category.objects.all()
    context = {
        'objects_list': category_list,
        'title': 'Список категорий продуктов'
    }
    return render(request, 'catalog/index.html', context)


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


def products(request):
    product_list = Product.objects.all()
    modified_product_list = []
    for product in product_list:
        modified_product = product
        modified_product.description = product.description[:100]
        modified_product_list.append(modified_product)
    context = {
        'objects_list': modified_product_list,
        'title': 'Список продуктов'
    }
    return render(request, 'catalog/product.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'catalog/product_details.html', {'product': product})
