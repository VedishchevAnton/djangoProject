from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify
from catalog.models import Category, Product, Contacts, Blogs


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


class ContactCreateView(generic.CreateView):
    model = Contacts
    template_name = "catalog/contact.html"
    fields = ('name', 'email', 'message')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Наши контакты"
        return context_data


class BlogsListView(generic.ListView):
    model = Blogs
    queryset = Blogs.objects.filter(is_published=True)
    context_object_name = 'blogs'
    paginate_by = 10


class BlogsDetailView(generic.DetailView):
    model = Blogs

    def get(self, request, *args, **kwargs):
        # Получаем объект статьи
        self.object = self.get_object()
        # Увеличиваем счетчик просмотров
        self.object.blog_views += 1
        # Сохраняем изменения в базе данных
        self.object.save()
        # Вызываем метод get() родительского класса DetailView
        return super().get(request, *args, **kwargs)


class BlogCreateView(generic.CreateView):
    model = Blogs
    fields = ['name', 'slug', 'description', 'image', 'is_published', 'blog_views']
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


class BlogUpdateView(generic.UpdateView):
    model = Blogs
    fields = ['name', 'description', 'image']
    success_url = reverse_lazy('catalog:blogs')


class BlogsDeleteView(generic.DeleteView):
    model = Blogs
    success_url = reverse_lazy('catalog:blogs')
