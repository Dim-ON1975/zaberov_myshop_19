from catalog.models import Product, Contacts

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect


class DataMixin:
    paginate_by = 3


class ProductsListView(DataMixin, ListView):
    """ Отображение товаров """
    model = Product


class ProductDetailView(DetailView):
    """ Детальная информация о товарах """
    model = Product


class ContactsListView(ListView):
    """ Отображение контактных данных """
    model = Contacts


class ProductCreateView(CreateView):
    """ Добавление (создание) товара """
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    """ Редактирование товара """
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    """ Удаление товара """
    model = Product
    success_url = reverse_lazy('catalog:products')


def toggle_activity(request, pk):
    """ Активация/деактивация товара """
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:products'))
