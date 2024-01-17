import json

from django.shortcuts import render, redirect

from catalog.models import Product, Contacts, Category
from catalog.utils.utils import json_save
from .forms import ProductForm
from django.core.paginator import Paginator
import uuid


def index(request):
    """
    Вывод главной страницы
    :param request: Объект, хранящий информацию о запросе, object.
    :return: HTML-страницу 'index.html'
    """
    return render(request, 'catalog/base.html')


def show_products(request):
    product_list = Product.objects.all().order_by('-date_update')
    # Пагинация
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/products.html', {'page_obj': page_obj,
                                                     'product_list': product_list})


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


# def handle_uploaded_file(f):
#     """ Сохранение файлов на сервер """
#     name = f.name
#     ext = ''
#
#     if '.' in name:
#         ext = name[name.rindex('.'):]
#         name = name[:name.rindex('.')]
#
#     suffix = str(uuid.uuid4())
#     with open(f"media/products/{name}_{suffix}{ext}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def create(request):
    """ Заполнение данных о товаре через форму """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['img'])
            form.save()
            return redirect('check')
    else:
        form = ProductForm()
    return render(request, 'catalog/create.html', {'form': form})


def check(request):
    return render(request, 'catalog/check.html')
