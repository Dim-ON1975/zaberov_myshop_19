import json

from django.shortcuts import render

from catalog.models import Product, Contacts
from catalog.utils.utils import json_save


def index(request):
    """
    Вывод главной страницы
    :param request: Объект, хранящий информацию о запросе, object.
    :return: HTML-страницу 'index.html'
    """
    return render(request, 'catalog/index.html')


def show_products(request):
    product_list = Product.objects.all().order_by('-date_update')[:5]
    return render(request, 'catalog/products.html', {'product_list': product_list})


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
