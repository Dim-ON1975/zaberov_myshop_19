from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blog.apps import BlogConfig
from blog.models import Post

app_name = BlogConfig.name

urlpatterns = [
    # Посты в блоге
    path('', PostListView.as_view(), name='view'),
    # Отдельный пост
    path('blog/<int:pk>/', PostDetailView.as_view(), name='detail'),
    # добавление поста через форму
    path('create/', PostCreateView.as_view(), name='create'),
    # редактирование поста через форму
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    # удаление поста
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete')
]
