from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from catalog.models import Category, Product, Contacts


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'objects_list'
    extra_context = {
        'title': 'Список категорий продуктов'
    }


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'objects_list'
    extra_context = {'title': 'Список продуктов'}

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            product.description = product.description[:100]
        return queryset


class ProductsDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = context_data['object']
        return context_data


class ProductsCreatView(generic.CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price')
    success_url = reverse_lazy('catalog:products')


class ProductsUpdateView(generic.UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price')
    success_url = reverse_lazy('catalog:products')


class ProductsDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


# def contact(request):
#     # Если метод запроса POST, значит пользователь отправил сообщение через форму контактов
#     if request.method == 'POST':
#         # Получаем данные из формы контактов (имя, email и сообщение)
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'Name: {name}\nEmail: {email}\nMessage: {message}')
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contact.html', context)
class ContactCreateView(generic.CreateView):
    model = Contacts
    template_name = "catalog/contact.html"
    fields = ('name', 'email', 'message')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Наши контакты"
        return context_data
