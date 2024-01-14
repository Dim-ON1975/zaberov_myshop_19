from django.urls import path
from . import views

urlpatterns = [
    # # главная страница
    # path('', views.index, name='index'),
    # продукты
    path('', views.show_products, name='products'),
    # контакты
    path('contacts/', views.contacts, name='contacts')
]
