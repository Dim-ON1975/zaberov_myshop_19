from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    """ Посты """
    title = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=250, **NULLABLE, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    img = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='превью')
    published_at = models.DateTimeField(default=timezone.now, verbose_name='дата публикации')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='опубликован')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
