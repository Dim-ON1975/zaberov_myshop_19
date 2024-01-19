import json

from django.shortcuts import render, redirect

from catalog.models import Product, Contacts, Category
from catalog.utils.utils import json_save
from .forms import ProductForm
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
import uuid


# def index(request):
#     """
#     Вывод главной страницы
#     :param request: Объект, хранящий информацию о запросе, object.
#     :return: HTML-страницу 'index.html'
#     """
#     return render(request, 'catalog/base.html')

class DataMixin:
    paginate_by = 3


class ProductsListView(DataMixin, ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsListView(ListView):
    model = Contacts


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
