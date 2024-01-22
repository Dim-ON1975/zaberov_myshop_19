from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'created_at', 'updated_at', 'is_published', 'view_count')
    list_filter = ('published_at', 'created_at', 'updated_at', 'is_published', 'view_count')
    search_fields = ('title', 'body',)
