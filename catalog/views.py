import json

from django.shortcuts import render

from catalog.models import Product, Contacts, Category
from catalog.utils.utils import json_save


def index(request):
    """
    Вывод главной страницы
    :param request: Объект, хранящий информацию о запросе, object.
    :return: HTML-страницу 'index.html'
    """
    return render(request, 'catalog/base.html')


def show_products(request):
    product_list = Product.objects.all().order_by('-date_update')[:6]
    return render(request, 'catalog/products.html', {'product_list': product_list})


def product_item(request, pk):
    product = Product.objects.get(pk=pk)
    category = Category.objects.get(pk=product.category_id)
    return render(request, 'catalog/product.html', {'product': product, 'category': category})


def contacts(request):
    """
    Вывод страницы "Контактные данные"
    :param request: Объект, хранящий информацию о запросе, object.
    :return: HTML-страницу 'contacts.html'
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        json_save(name, phone, message)
    contacts_list = Contacts.objects.all().order_by('pk')
    return render(request, 'catalog/contacts.html', {'contacts_list': contacts_list})
