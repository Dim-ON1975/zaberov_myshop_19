from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_publish', 'date_created', 'date_updated', 'status', 'view_count')
    list_filter = ('date_publish', 'date_created', 'date_updated', 'status', 'view_count')
    search_fields = ('title', 'body',)
