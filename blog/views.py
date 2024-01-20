from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from blog.models import Post


class DataMixin:
    paginate_by = 3


class PostListView(DataMixin, ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:view')


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:view')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:view')
