from django.contrib import admin

from catalog.models import Category, Product, Contacts, Version


# Register your models here.
# admin.py
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')  # вывод полей в админке
    list_filter = ('name',)  # фильтрация в админке
    search_fields = ('name',)  # поиск по указанным полям


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'is_active')
    list_filter = ('category', 'price', 'is_active')
    search_fields = ('name', 'category', 'price',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'position', 'phone', 'email',)
    list_filter = ('last_name', 'first_name',)
    search_fields = ('first_name', 'last_name', 'position', 'phone', 'email',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'num_version', 'name_version', 'is_active',)
    list_filter = ('num_version', 'name_version', 'is_active',)
    search_fields = ('product', 'num_version', 'name_version', 'is_active',)
