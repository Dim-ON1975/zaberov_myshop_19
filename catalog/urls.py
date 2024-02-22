from django.urls import path
from catalog.views import ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactsListView, toggle_activity, ProductsUserListView, CategoryListView
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page, never_cache

from .models import Product

app_name = CatalogConfig.name

urlpatterns = [
    # продукты в обратном порядке по дате изменения - главная страница
    path('<int:pk>/', ProductsListView.as_view(), name='products'),
    path('account/products/<int:pk>/', ProductsUserListView.as_view(), name='products_user'),
    # категории продуктов
    path('category/', CategoryListView.as_view(), name='category'),
    # продукт
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    # контакты
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    # добавление продукта через форму
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    # редактирование продукта через форму
    path('update/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='update'),
    # удаление товара
    path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='delete'),
    # активация/деактивация товара
    path('activity/<int:pk>', never_cache(toggle_activity), name='activity')
]
