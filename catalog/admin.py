from django.contrib import admin

from catalog.models import Category, Product, Contacts


# Register your models here.
# admin.py
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')  # вывод полей в админке
    list_filter = ('name',)  # фильтрация в админке
    search_fields = ('name',)  # поиск по указанным полям


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price',)
    list_filter = ('category', 'price',)
    search_fields = ('name', 'category', 'price',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'position', 'phone', 'email',)
    list_filter = ('last_name', 'first_name',)
    search_fields = ('first_name', 'last_name', 'position', 'phone', 'email',)
