from django.urls import path
from . import views

urlpatterns = [
    # главная страница
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts')
]