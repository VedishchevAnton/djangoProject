from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    # Если метод запроса POST, значит пользователь отправил сообщение через форму контактов
    if request.method == 'POST':
        # Получаем данные из формы контактов (имя, email и сообщение)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}\nEmail: {email}\nMessage: {message}')
    return render(request, 'catalog/contact.html')
