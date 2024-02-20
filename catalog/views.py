from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.forms.models import inlineformset_factory
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404

from core.settings import LOGIN_URL


class ProductsListView(ListView):
    """ Отображение товаров """
    model = Product
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.order_by("-is_active", "-updated_at").filter(is_published=True).distinct()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version_list'] = Version.objects.get_queryset(**kwargs)
        return context_data


class ProductsUserListView(LoginRequiredMixin, ListView):
    """ Отображение товаров """
    model = Product
    template_name = 'catalog/product_user_list.html'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.groups.filter(name='moderators').exists():
            queryset = queryset.order_by("-is_published", "-is_active", "-updated_at").distinct()
        else:
            queryset = queryset.order_by("-is_published", "-is_active", "-updated_at").filter(
                user=self.request.user).distinct()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version_list'] = Version.objects.get_queryset(**kwargs)
        return context_data


class ProductDetailView(DetailView):
    """ Детальная информация о товарах """
    model = Product


class ContactsListView(ListView):
    """ Отображение контактных данных """
    model = Contacts


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Добавление (создание) товара """
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:products_user')

    def form_valid(self, form):
        # Получаем текущего пользователя
        user = self.request.user
        # Присваиваем текущего пользователя полю user нового продукта
        form.instance.user = user
        # Сохраняем экземпляр модели перед вызовом super().form_valid()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # Получаем ключевые аргументы для формы
        kwargs = super().get_form_kwargs()
        # Изменяем аргументы формы, добавляя пользователя в их начальные значения
        kwargs['initial'] = {'user': self.request.user}
        return kwargs


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Редактирование товара """
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.crate_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            messages.error(self.request, 'Выберете только одну активную версию')
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Удаление товара """
    model = Product
    success_url = reverse_lazy('catalog:products')
    permission_required = 'catalog.delete_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user


@login_required
@user_passes_test(lambda u: lambda product_id: u == get_object_or_404(Product, pk=product_id).user, login_url=LOGIN_URL)
def toggle_activity(request, pk):
    """ Активация/деактивация товара """
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:products'))
