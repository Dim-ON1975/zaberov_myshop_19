from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.forms.models import inlineformset_factory
from django.contrib import messages


class ProductsListView(ListView):
    """ Отображение товаров """
    model = Product
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.order_by("-is_active", "-updated_at").distinct()
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


class ProductCreateView(CreateView):
    """ Добавление (создание) товара """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    """ Редактирование товара """
    model = Product
    form_class = ProductForm

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

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            messages.error(self.request, 'Выберете только одну активную версию')
        return super().form_valid(form)


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
