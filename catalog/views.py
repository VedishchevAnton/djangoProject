from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.urls import reverse_lazy
from django.views import generic
from django.utils.text import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Contacts, Blogs, Version
from catalog.services import get_cached_product_data


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']
        for product in products:
            product.get_active_version()
        return context


class ProductsDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)  # Получаем контекст данных из родительского класса
        cached_data = get_cached_product_data(self.object)
        context_data.update(cached_data)
        return context_data


class ProductsCreatView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    # permission_required = 'catalog.add_product'З

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save(commit=False)
        self.object.product_owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    # permission_required = 'catalog.change_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.product_owner != self.request.user:
            raise Http404("Вы не являетесь владельцем продукта.")
        return obj

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        if not self.request.user.has_perm('catalog.can_change_product_description'):
            return HttpResponseForbidden("You don't have permission to change product description.")
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')

    # permission_required = 'catalog.delete_product'

    def test_func(self):
        return self.request.user.is_superuser  # жесткие требования на удаление ( только суперюзер может удалить)


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

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('catalog:blog_details', kwargs={'pk': pk})


class BlogsDeleteView(generic.DeleteView):
    model = Blogs
    success_url = reverse_lazy('catalog:blogs')
