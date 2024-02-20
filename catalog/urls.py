from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsListView, toggle_activity, ProductsUserListView
from catalog.apps import CatalogConfig

from .models import Product

app_name = CatalogConfig.name

urlpatterns = [
    # продукты в обратном порядке по дате изменения - главная страница
    path('', ProductsListView.as_view(), name='products'),
    path('account/products/', ProductsUserListView.as_view(), name='products_user'),
    # продукт
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # контакты
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    # добавление продукта через форму
    path('create/', ProductCreateView.as_view(), name='create'),
    # редактирование продукта через форму
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    # удаление товара
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    # активация/деактивация товара
    path('activity/<int:pk>', toggle_activity, name='activity')
]
