from django.db import models
from django.core.validators import MinValueValidator

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """ Категории товаров """
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)  # Фильтрация


class Product(models.Model):
    """ Товары (продукты) """
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    img = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='цена')
    date_add = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='наличие товара')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'category', 'price', 'date_add', 'date_update', 'is_active')


class Contacts(models.Model):
    """ Контактные данные организации """
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    position = models.CharField(max_length=100, verbose_name='должность')
    phone = models.CharField(max_length=18, verbose_name='телефон')
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.position}, {self.phone}, {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('first_name', 'last_name', 'position', 'phone', 'email')


