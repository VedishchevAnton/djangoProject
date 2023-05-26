from django.shortcuts import render

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


def product(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list,
        'title': 'Список продуктов'
    }
    return render(request, 'catalog/product.html', context)


def product_detail(request, product_id):
    product_data = Product.objects.get(id=product_id)
    context = {'product': product_data}
    return render(request, 'catalog/product_detail.html', context)
