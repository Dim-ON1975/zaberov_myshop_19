from django.db import models
from django.core.validators import MinValueValidator
from django import forms

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """ Категории товаров """
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)  # Фильтрация


class Version(models.Model):
    """ Версия продукта """
    NUMBER_VERSION_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
    )
    VERSION_CHOICES = (
        ("базовая", "базовая"),
        ("новинка", "новинка"),
        ("распродажа", "распродажа"),
        ("скидка", "скидка"),
        ("витрина", "витрина"),
        ("уценённый", "уценённый"),
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    num_version = models.PositiveIntegerField(choices=NUMBER_VERSION_CHOICES, default='1',
                                              verbose_name='номер')
    name_version = models.CharField(max_length=10, choices=VERSION_CHOICES, default='базовая',
                                    verbose_name='название')
    is_active = models.BooleanField(default=False, verbose_name='активная')

    def __str__(self):
        return f'{self.product}'

    # def save(self, *args, **kwargs):
    #     if self.is_active:
    #         Version.objects.filter(product=self.product).exclude(pk=self.pk).update(is_active=False)
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product', 'num_version', 'name_version', 'is_active')


class Product(models.Model):
    """ Товары (продукты) """
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    img = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='наличие товара')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'category', 'price', 'created_at', 'updated_at', 'is_active')


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
