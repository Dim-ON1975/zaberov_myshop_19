from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'last_name', 'first_name', 'phone', 'is_staff', 'is_active', 'is_superuser',
        'email_verify',)
    list_filter = ('last_name', 'email', 'email_verify', 'is_staff', 'is_active', 'is_superuser',)
    search_fields = ('last_name', 'first_name', 'email',)
