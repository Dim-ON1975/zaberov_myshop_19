from django.urls import path
from account.apps import AccountConfig
from django.contrib.auth.views import LoginView, LogoutView
from account.views import RegisterView, ProfileUpdateView, ProfileDetailView, UserDeleteView

app_name = AccountConfig.name

urlpatterns = [
    # Авторизация
    path('', LoginView.as_view(), name='login'),
    # Выход
    path('logout/', LogoutView.as_view(), name='logout'),
    # Регистрация
    path('register/', RegisterView.as_view(), name='register'),
    # Редактирование профиля
    path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
    # Просмотр профиля
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    # Удаление профиля
    path('delete_profile/', UserDeleteView.as_view(), name='user_delete'),

]
