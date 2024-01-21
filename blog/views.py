from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Post


class DataMixin:
    paginate_by = 3


class PostListView(DataMixin, ListView):
    """ Список постов """
    model = Post

    def get_queryset(self, *args, **kwargs):
        """ Отображение только опубликованных постов (фильтрация по полю status """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(status=True)
        return queryset


class PostDetailView(DetailView):
    """ Пост """
    model = Post

    def get_object(self, queryset=None):
        """" Счётчик просмотров """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    """ Форма создания поста """
    model = Post
    fields = ('title', 'body', 'img', 'date_publish', 'status')
    success_url = reverse_lazy('blog:view')

    def form_valid(self, form):
        """ Формирование слага """
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """ Форма редактирования поста """
    model = Post
    fields = ('title', 'body', 'img', 'date_publish', 'status')

    def form_valid(self, form):
        """ Формирование слага """
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        """ Перенаправление на пост """
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    """ Удаление поста """
    model = Post
    success_url = reverse_lazy('blog:view')
