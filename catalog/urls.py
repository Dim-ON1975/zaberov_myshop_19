from django.urls import path
from . import views

urlpatterns = [
    # # главная страница
    # path('', views.index, name='index'),
    # продукты - главная страница
    path('', views.show_products, name='products'),
    # продукт
    path('catalog/<int:pk>/', views.product_item, name='product'),
    # контакты
    path('contacts/', views.contacts, name='contacts'),
    # добавление продукта через форму
    path('create/', views.create, name='create'),
    path('check/', views.check, name='check')
]
