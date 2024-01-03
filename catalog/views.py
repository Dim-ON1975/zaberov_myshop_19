from django.shortcuts import render

from catalog.utils.utils import json_save


def index(request):
    """
    Вывод главной страницы
    :param request: Объект, хранящий информацию о запросе, object.
    :return: HTML-страницу 'index.html'
    """
    return render(request, 'catalog/index.html')


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
    return render(request, 'catalog/contacts.html')
